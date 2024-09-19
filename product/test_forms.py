from django.test import TestCase
from .forms import ProductForm


# Create forms tests here.

class TestProductForm(TestCase):
    """
    Test Product Form
    """

    def test_product_form_is_valid(self):
        """
        Test form is valid if all fields are
        correctly submitted
        """
        form = ProductForm(
            data={
                "name": "Product B",
                "price": 50000,
                "currency": "USD",
            })
        self.assertTrue(form.is_valid())

    def test_product_form_is_not_valid(self):
        """
        Test form if an undefined field is submitted
        """
        form = ProductForm(
            data={
                "names": "Product B",
                "price": 50000,
                "currency": "USD",
            })
        self.assertFalse(form.is_valid())

    def test_product_form_is_not_valid_empty_field(self):
        """
        Test form if an empty field is submitted
        """
        form = ProductForm(
            data={
                "price": 50000,
                "currency": "USD",
            })
        self.assertFalse(form.is_valid())
