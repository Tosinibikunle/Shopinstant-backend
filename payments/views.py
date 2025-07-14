# payments/views.py

import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
PAYSTACK_INITIALIZE_URL = "https://api.paystack.co/transaction/initialize"
PAYSTACK_VERIFY_URL = "https://api.paystack.co/transaction/verify/{}"


class InitializePaymentView(View):
    def post(self, request):
        data = request.POST
        email = data.get('email')
        amount = data.get('amount')  # amount in kobo (NGN minor unit)

        if not email or not amount:
            return HttpResponseBadRequest("Email and amount are required.")

        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "email": email,
            "amount": int(amount),
            "callback_url": "https://your-frontend-domain.com/payment/callback/",
        }

        response = requests.post(PAYSTACK_INITIALIZE_URL, json=payload, headers=headers)
        res_data = response.json()

        if res_data.get("status"):
            return JsonResponse({"authorization_url": res_data['data']['authorization_url']})
        else:
            return JsonResponse({"error": res_data.get("message")}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class VerifyPaymentView(View):
    def get(self, request, reference):
        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        }
        url = PAYSTACK_VERIFY_URL.format(reference)
        response = requests.get(url, headers=headers)
        res_data = response.json()

        if res_data.get("status") and res_data['data']['status'] == "success":
            # Payment successful - update order/payment status accordingly
            return JsonResponse({"message": "Payment verified successfully.", "data": res_data['data']})
        else:
            return JsonResponse({"error": "Payment verification failed."}, status=400)
