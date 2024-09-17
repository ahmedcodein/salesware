from django.test import TestCase
from django.urls import reverse, resolve
from .views import (ProspectList, prospect_detail,
                    prospect_create, prospect_edit,
                    prospect_delete)


# Create your tests here for product urls
class TestProductUrls(TestCase):
    # Test product urls Class
    def test_prospect_list(self):
        # Test ProspectList Class view
        url = reverse('prospect_list')
        self.assertEqual(resolve(url).func.view_class, ProspectList)

    def test_prospect_detail(self):
        # Test prospect_detail function view
        url = reverse('prospect_detail', args=[1])
        self.assertEqual(resolve(url).func, prospect_detail)

    def test_prospect_create(self):
        # Test prospect_create function view
        url = reverse('prospect_create')
        self.assertEqual(resolve(url).func, prospect_create)

    def test_prospect_edit(self):
        # Test prospect_edit function view
        url = reverse('prospect_edit')
        self.assertEqual(resolve(url).func, prospect_edit)

    def test_prospect_delete(self):
        # Test prospect_delete function view
        url = reverse('prospect_delete')
        self.assertEqual(resolve(url).func, prospect_delete)
