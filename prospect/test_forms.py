from django.test import TestCase
from .forms import ProspectForm


# Create forms tests here.

class TestProspectForm(TestCase):
    """
    Test Prospect Form
    """

    def test_prospect_form_is_valid(self):
        """
        Test form is valid if all field
        correctly submitted
        """
        form = ProspectForm(
            data={
                'company': "A GmbH",
                'first_name': "john",
                'last_name': "Neil",
                'email': "john.neil@email.com",
                'title': "Head of Sales",
                'industry': "Telecommunication",
                'country': 'UK',
            })
        self.assertTrue(form.is_valid())

    def test_prospect_form_is_not_valid(self):
        """
        Test form if an undefined field is submitted
        """
        form = ProspectForm(
            data={
                'test': "A GmbH",
                'first_name': "john",
                'last_name': "Neil",
                'email': "john.neil@email.com",
                'title': "Head of Sales",
                'industry': "Telecommunication",
            })
        self.assertFalse(form.is_valid())

    def test_prospect_form_is_not_valid_empty_field(self):
        """
        Test form if an empty field is submitted
        """
        form = ProspectForm(
            data={
                'first_name': "john",
                'last_name': "Neil",
                'email': "john.neil@email.com",
                'title': "Head of Sales",
                'industry': "Telecommunication",
            })
        self.assertFalse(form.is_valid())
