from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Prospect

# Create your tests here for prospect views


class TestProspectViews(TestCase):
    """
    Test prospect views class
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
        # Create a prospect object
        self.prospect = Prospect.objects.create(
            company="A GmbH",
            first_name="john",
            last_name="will",
            email="john.will@email.com",
            title="Head of Sales",
            industry="IT",
            country="Germany",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        # Establish url links
        # prospect list
        self.prospect_list_url = reverse('prospect_list')
        self.prospect_list_template_name = 'prospect/prospect_list.html'
        # prospect detail
        self.prospect_detail_url = reverse(
            'prospect_detail', args=[self.prospect.id])
        self.prospect_detail_template_name = 'prospect/prospect_detail.html'
        # prospect create
        self.prospect_create_url = reverse(
            'prospect_create'
        )
        # prospect edit
        self.prospect_edit_url = reverse(
            'prospect_edit'
        )
        # prospect delete
        self.prospect_delete_url = reverse(
            'prospect_delete'
        )

    def test_prospect_list_view(self):
        """
        Test ProspectList view class
        """
        response = self.client.get(self.prospect_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.prospect_list_template_name)

    def test_prospect_detail_view(self):
        """
        Test prospect_detail view function
        """
        response = self.client.get(self.prospect_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.prospect_detail_template_name)

    def test_prospect_create_view(self):
        """
        Test prospect_create view function
        """
        response = self.client.post(self.prospect_create_url, {
            'company': "B GmbH",
            'first_name': "john",
            'last_name': "shall",
            'email': "john.shall@email.com",
            'title': "Sales Manager",
            'industry': "IT",
            'country': 'Germany',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(Prospect.objects.latest(
            'id').company, self.prospect.company)
        self.assertEqual(Prospect.objects.latest(
            'id').company, 'B GMBH')

    def test_prospect_edit_view(self):
        """
        Test prospect_edit view function
        """
        self.session['prospect_id'] = self.prospect.id
        self.session.save()
        response = self.client.post(self.prospect_edit_url, {
            'company': "B GmbH",
            'first_name': "john",
            'last_name': "Neil",
            'email': "john.neil@email.com",
            'title': "Head of Sales",
            'industry': "Telecommunication",
            'country': 'UK',
        })
        self.prospect.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.prospect.country, 'Germany')

    def test_prospect_delete_view(self):
        """
        Test prospect_delete view function
        """
        self.session['prospect_id'] = self.prospect.id
        self.session.save()
        # test prospect exists before deletion
        self.assertTrue(Prospect.objects.filter(id=self.prospect.id).exists())
        response = self.client.post(self.prospect_delete_url)
        self.assertEqual(response.status_code, 200)
        # test prospect does not exist before deletion
        self.assertFalse(Prospect.objects.filter(id=self.prospect.id).exists())
