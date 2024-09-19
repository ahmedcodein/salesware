from django.test import TestCase
from django.urls import reverse

# Create your tests here for communication views


class TestCommunicationViews(TestCase):
    """
    Test communication views class
    """

    def setUp(self):
        """
        Create the test initial set up
        """
        # Establish url links
        # home
        self.hom_url = reverse('home')
        self.home_template_name = (
            'communication/home.html'
        )

        # contact
        self.contact_url = reverse('contact')
        self.contact_template_name = (
            'communication/contact.html'
        )

    def test_home_view(self):
        """
        Test home view class
        """
        response = self.client.get(self.hom_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, self.home_template_name
        )

    def test_contact_view(self):
        """
        Test contact view class
        """
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, self.contact_template_name
        )
