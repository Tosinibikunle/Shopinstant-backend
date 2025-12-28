
import requests
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

# Configuration
# Ensure PAYSTACK_SECRET_KEY is set in your settings.py file
PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
PAYSTACK_INITIALIZE_URL = "https://api.paystack.co/transaction/initialize"
PAYSTACK_VERIFY_URL = "https://api.paystack.co/transaction/verify/{}"


class InitializePaymentView(View):
    """
    Initiates a transaction with Paystack.
    
    This view receives an email and an amount from the client, sends it to Paystack,
    and returns an 'authorization_url' where the user can enter their card details.
    """

    def post(self, request):
        # NOTE: If your frontend (React/Vue) sends JSON, request.POST might be empty.
        # You might need: data = json.loads(request.body)
        data = request.POST
        
        email = data.get('email')
        amount = data.get('amount') 

        if not email or not amount:
            return HttpResponseBadRequest("Email and amount are required.")

        # Paystack Authentication Headers
        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        # IMPORTANT: Paystack expects amount in Kobo (Naira * 100).
        # Example: NGN 100.00 -> 10000 kobo.
        # Ensure 'amount' passed here is already calculated or multiply it by 100.
        payload = {
            "email": email,
            "amount": int(amount), 
            "callback_url": "https://your-frontend-domain.com/payment/callback/", # Update this!
        }

        try:
            # Make the request to Paystack API
            response = requests.post(
                PAYSTACK_INITIALIZE_URL, json=payload, headers=headers
            )
            res_data = response.json()

            # If Paystack returns success, send the payment URL to the frontend
            if res_data.get("status"):
                return JsonResponse({"authorization_url": res_data['data']['authorization_url']})
            else:
                return JsonResponse({"error": res_data.get("message")}, status=400)
        
        except requests.exceptions.RequestException as e:
            # Handle network errors (e.g., Paystack is down)
            return JsonResponse({"error": str(e)}, status=503)


# We disable CSRF protection here because this might be called by external services
# or mobile apps where CSRF tokens are difficult to manage.
@method_decorator(csrf_exempt, name='dispatch')
class VerifyPaymentView(View):
    """
    Verifies a transaction after the user has returned from Paystack.
    
    The frontend should send the 'reference' code here to confirm the payment
    was actually successful on Paystack's end.
    """

    def get(self, request, reference):
        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        }
        
        # Format the URL with the unique transaction reference
        url = PAYSTACK_VERIFY_URL.format(reference)
        
        try:
            response = requests.get(url, headers=headers)
            res_data = response.json()

            # Check if the transaction status is explicitly 'success'
            if res_data.get("status") and res_data['data']['status'] == "success":
                # Payment is confirmed!
                # TODO: Add logic here to update your Order model.
                # Example:
                # order = Order.objects.get(ref=reference)
                # order.is_paid = True
                # order.save()
                
                return JsonResponse({
                    "message": "Payment verified successfully.", 
                    "data": res_data['data']
                })
            else:
                return JsonResponse({"error": "Payment verification failed."}, status=400)

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": "Network error verifying payment."}, status=503)
