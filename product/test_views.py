from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Product

# Create your tests here for product views


class TestProductViews(TestCase):
    """
    Test product views class
    """
    def setUp(self):
        # Create a test scenario
        self.client = Client()
        # Create a user
        self.user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
        # Ensure user is logged in and established
        # a session
        self.client.force_login(self.user)
        self.session = self.client.session
        # Create a product object
        self.product = Product.objects.create(
            name="Product A",
            price=50000,
            currency="EUR",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        # Establish url links
        # product list
        self.product_list_url = reverse('product_list')
        self.product_list_template_name = 'product/product_list.html'
        # product detail
        self.product_detail_url = reverse(
            'product_detail', args=[self.product.id])
        self.product_detail_template_name = 'product/product_detail.html'
        # product create
        self.product_create_url = reverse(
            'product_create'
        )
        # product edit
        self.product_edit_url = reverse(
            'product_edit'
        )
        # product delete
        self.product_delete_url = reverse(
            'product_delete'
        )

    def test_product_list_view(self):
        """
        Test ProductList view class
        """
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.product_list_template_name)

    def test_product_detail_view(self):
        """
        Test product_detail view function
        """
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.product_detail_template_name)

    def test_product_create_view(self):
        """
        Test product_create view function
        """
        response = self.client.post(self.product_create_url, {
            "name": "Product B",
            "price": 50000,
            "currency": "USD",
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(Product.objects.latest(
            'id').name, self.product.name)
        self.assertEqual(Product.objects.latest(
            'id').name, 'PRODUCT B')

    def test_product_edit_view(self):
        """
        Test product_edit view function
        """
        self.session['product_id'] = self.product.id
        self.session.save()
        response = self.client.post(self.product_edit_url, {
            "name": "Product C",
            "price": 100000,
            "currency": "GBP",
        })
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product.price, 100000)
        self.assertNotEqual(self.product.currency, 'EUR')

    def test_product_delete_view(self):
        """
        Test product_delete view function
        """
        self.session['product_id'] = self.product.id
        self.session.save()
        # test product exists before deletion
        self.assertTrue(Product.objects.filter(id=self.product.id).exists())
        response = self.client.post(self.product_delete_url)
        self.assertEqual(response.status_code, 200)
        # test product does not exist before deletion
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
