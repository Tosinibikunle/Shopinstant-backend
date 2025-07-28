from django.test import TestCase
from .models import ShippingMethod


class ShippingMethodTestCase(TestCase):
    def setUp(self):
        # Set up initial test data
        ShippingMethod.objects.create(
            name="Standard", cost=10.00, estimated_days=5)
        ShippingMethod.objects.create(
            name="Express", cost=25.00, estimated_days=2)

    def test_shipping_method_count(self):
        """Ensure two shipping methods exist."""
        self.assertEqual(ShippingMethod.objects.count(), 2)

    def test_shipping_method_names(self):
         """Verify the names of shipping methods."""
         standard = ShippingMethod.objects.get(name="Standard")
         express = ShippingMethod.objects.get(name="Express")
         self.assertEqual(str(standard), "Standard")
         self.assertEqual(str(express), "Express")

    def test_shipping_cost(self):
        """Check that the cost is stored correctly."""
        express = ShippingMethod.objects.get(name="Express")
        self.assertEqual(express.cost, 25.00)
