from django.test import TestCase
from django.urls import reverse, resolve
from .views import (OpportunityList, opportunity_detail,
                    opportunity_create, opportunity_edit,
                    opportunity_delete)


# Create your tests here for opportunity urls
class TestOpportunityUrls(TestCase):
    # Test opportunity urls Class
    def test_opportunity_list(self):
        # Test OpportunityList Class view
        url = reverse('opportunity_list')
        self.assertEqual(resolve(url).func.view_class, OpportunityList)

    def test_opportunity_detail(self):
        # Test opportunity_detail function view
        url = reverse('opportunity_detail', args=[1])
        self.assertEqual(resolve(url).func, opportunity_detail)

    def test_opportunity_create(self):
        # Test opportunity_create function view
        url = reverse('opportunity_create')
        self.assertEqual(resolve(url).func, opportunity_create)

    def test_opportunity_edit(self):
        # Test opportunity_edit function view
        url = reverse('opportunity_edit')
        self.assertEqual(resolve(url).func, opportunity_edit)

    def test_opportunity_delete(self):
        # Test opportunity_delete function view
        url = reverse('opportunity_delete')
        self.assertEqual(resolve(url).func, opportunity_delete)
