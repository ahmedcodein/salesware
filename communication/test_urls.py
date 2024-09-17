from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, contact

# Create your tests here for communication urls


class TestCommunicationUrls(TestCase):
    # Test communication urls Class
    def test_home_view(self):
        # Test home function view
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_contact_view(self):
        # Test contact function view
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
