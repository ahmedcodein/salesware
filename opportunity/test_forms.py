from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from prospect.models import Prospect
from product.models import Product
from .forms import OpportunityForm


# Create forms tests here.

class TestOpportunityForm(TestCase):
    """
    Test Opportunity Form
    """

    def setUp(self):
        """
        Establish a test scenario
        """
        # Create a user
        self.user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
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

    def test_opportunity_form_is_valid(self):
        """
        Test form is valid if all fields are
        correctly submitted
        """
        form = OpportunityForm(
            data={
                'name': 'Opportunity One',
                'lead': self.prospect.id,
                'solution': self.product.id,
                'note': 'Opportunity is for test',
                'probability': 25,
                'sales_stage': 'Negotiation',
                'status': 'In Progress',
            })
        self.assertTrue(form.is_valid())

    def test_opportunity_form_is_not_valid(self):
        """
        Test form if an undefined field is submitted
        """
        form = OpportunityForm(
            data={
                'names': 'Opportunity One',
                'lead': self.prospect.id,
                'solution': self.product.id,
                'note': 'Opportunity is for test',
                'probability': 25,
                'sales_stage': 'Negotiation',
                'status': 'In Progress',
            })
        self.assertFalse(form.is_valid())

    def test_opportunity_form_is_not_valid_empty_field(self):
        """
        Test form if an empty field is submitted
        """
        form = OpportunityForm(
            data={
                'solution': self.product.id,
                'note': 'Opportunity is for test',
                'probability': 25,
                'sales_stage': 'Negotiation',
                'status': 'In Progress',
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
