from django.test import TestCase
from django.urls import reverse, resolve
from .views import (ProductList, product_detail,
                    product_create, product_edit,
                    product_delete)


# Create your tests here for product urls
class TestProductUrls(TestCase):
    # Test Product urls Class
    def test_product_list(self):
        # Test productList Class view
        url = reverse('product_list')
        self.assertEqual(resolve(url).func.view_class, ProductList)

    def test_product_detail(self):
        # Test product_detail function view
        url = reverse('product_detail', args=[1])
        self.assertEqual(resolve(url).func, product_detail)

    def test_product_create(self):
        # Test product_create function view
        url = reverse('product_create')
        self.assertEqual(resolve(url).func, product_create)

    def test_product_edit(self):
        # Test product_edit function view
        url = reverse('product_edit')
        self.assertEqual(resolve(url).func, product_edit)

    def test_product_delete(self):
        # Test product_delete function view
        url = reverse('product_delete')
        self.assertEqual(resolve(url).func, product_delete)
