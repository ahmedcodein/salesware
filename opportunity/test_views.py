from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Opportunity
from prospect.models import Prospect
from product.models import Product

# Create your tests here for opportunity views


class TestOpportunityViews(TestCase):
    """
    Test opportunity views class
    """

    def setUp(self):
        """
        Create a test scenario
        """
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
        # Create a product object
        self.product = Product.objects.create(
            name="Product A",
            price=50000,
            currency="EUR",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        # Create an opportunity object
        self.opportunity = Opportunity.objects.create(
            name='Test Opportunity',
            lead=self.prospect,
            solution=self.product,
            note='Opportunity is for test',
            probability=25,
            sales_stage='lead',
            is_closed=False,
            status='In Progress',
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        # Establish url links
        # opportunity list
        self.opportunity_list_url = reverse('opportunity_list')
        self.opportunity_list_template_name = (
            'opportunity/opportunity_list.html'
        )

        # opportunity detail
        self.opportunity_detail_url = reverse(
            'opportunity_detail', args=[self.opportunity.id]
        )
        self.opportunity_detail_template_name = (
            'opportunity/opportunity_detail.html'
        )
        # opportunity create
        self.opportunity_create_url = reverse(
            'opportunity_create'
        )
        # opportunity edit
        self.opportunity_edit_url = reverse(
            'opportunity_edit'
        )
        # opportunity delete
        self.opportunity_delete_url = reverse(
            'opportunity_delete'
        )

    def test_opportunity_list_view(self):
        """
        Test OpportunityList view class
        """
        response = self.client.get(self.opportunity_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, self.opportunity_list_template_name
        )

    def test_opportunity_detail_view(self):
        """
        Test opportunity_detail view function
        """
        response = self.client.get(self.opportunity_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, self.opportunity_detail_template_name
        )

    def test_opportunity_create_view(self):
        """
        Test opportunity_create view function
        """
        response = self.client.post(self.opportunity_create_url, {
            'name': 'Opportunity One',
            'lead': self.prospect.id,
            'solution': self.product.id,
            'note': 'Opportunity is for test',
            'probability': 25,
            'sales_stage': 'Negotiation',
            'status': 'In Progress',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(Opportunity.objects.latest(
            'id').name, self.opportunity.name)
        self.assertEqual(Opportunity.objects.latest(
            'id').name, 'OPPORTUNITY ONE')

    def test_opportunity_edit_view(self):
        """
        Test opportunity_edit view function
        """
        self.session['opportunity_id'] = self.opportunity.id
        self.session.save()
        response = self.client.post(self.opportunity_edit_url, {
            'name': 'Test Opportunity B',
            'lead': self.prospect.id,
            'solution': self.opportunity.id,
            'note': 'Opportunity is for test but updated',
            'probability': 75,
            'sales_stage': 'Negotiation',
            'status': 'In Progress',
        })
        self.opportunity.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.opportunity.sales_stage, 'Negotiation')
        self.assertNotEqual(self.opportunity.note, 'Opportunity is for test')

    def test_opportunity_delete_view(self):
        """
        Test opportunity_delete view function
        """
        self.session['opportunity_id'] = self.opportunity.id
        self.session.save()
        # test opportunity exists before deletion
        self.assertTrue(Opportunity.objects.filter(
            id=self.opportunity.id).exists())
        response = self.client.post(self.opportunity_delete_url)
        self.assertEqual(response.status_code, 200)
        # test opportunity does not exist before deletion
        self.assertFalse(Opportunity.objects.filter(
            id=self.opportunity.id).exists())
