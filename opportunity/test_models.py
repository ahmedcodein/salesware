from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from prospect.models import Prospect, UpperCaseConverter
from product.models import Product
from .models import Opportunity

# Create your tests here.


class OpportunityModelTest(TestCase):
    """
    Test the Opportunity Model
    """

    def setUp(self):
        # Create a User
        self.user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
        # Create a prospect
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
        # Create a product
        self.product = Product.objects.create(
            name="Product A",
            price=50000.00,
            currency="USD",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        # Create an opportunity
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

    def test_create_opportunity(self):
        # Test all Opportunity attributes' values
        self.assertEqual(self.opportunity.name, 'Test Opportunity')
        self.assertEqual(self.opportunity.lead.company, 'A GmbH')
        self.assertEqual(self.opportunity.solution.name, 'Product A')
        self.assertEqual(self.opportunity.status, 'In Progress')
        self.assertEqual(self.opportunity.note, 'Opportunity is for test')
        self.assertEqual(self.opportunity.probability, 25)
        self.assertEqual(self.opportunity.sales_stage, 'lead')
        self.assertFalse(self.opportunity.is_closed)
        self.assertEqual(self.opportunity.status, 'In Progress')
        self.assertEqual(self.opportunity.owner.username, 'TeamUser')
        self.assertIsInstance(self.opportunity.created_on, datetime)
        self.assertIsInstance(self.opportunity.updated_at, datetime)

    def test_upper_case_converter(self):
        # Test UpperCaseConverter Class on opportunity object
        opportunity_upper = UpperCaseConverter().get_prep_value(
            self.opportunity.name
        )
        assert opportunity_upper != self.opportunity.name

    def test_winning_probability_method(self):
        # Test winning_probability property method
        winning_probability = self.opportunity.winning_probability
        self.assertEqual(winning_probability, '25%')

    def test_estimation(self):
        # Test estimation property method
        est = self.opportunity.estimation
        self.assertEqual(est, str(self.product.price *
                                  self.opportunity.probability/100) +
                         ' ' + self.product.currency)
