from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Prospect, UpperCaseConverter


# Create your tests here.

class SuperUserModelTest(TestCase):
    """
    Test Django Superuser model
    """

    def test_create_superuser(self):
        # Create an instance of superuser class
        user = User.objects.create_superuser(
            username="AdminUser",
            email="super.user@email.com",
        )
        # Assert that each attribute is correctly defined
        self.assertEqual(user.username, "AdminUser")
        self.assertIsNotNone(user.password)
        self.assertEqual(user.email, "super.user@email.com")


class UserModelTest(TestCase):
    """
    Test Django user model
    """

    def test_create_user(self):
        user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
        self.assertEqual(user.username, "TeamUser")
        self.assertIsNotNone(user.password)
        self.assertEqual(user.email, "team.user@email.com")


class ProspectModelTest(TestCase):
    """
    Test prospect Model
    """

    def test_create_prospect(self):
        """
        Create User instance and two prospect instances
        """

        self.user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
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
        self.prospect_b = Prospect.objects.create(
            company="B GmbH",
            first_name="john",
            last_name="shall",
            email="john.shall@email.com",
            title="Sales Manager",
            industry="IT",
            country="Germany",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now()
        )
        # Assert that each attribute is accurately defined in
        # the prospect model
        self.assertEqual(self.prospect.company, "A GmbH")
        self.assertEqual(self.prospect.first_name, "john")
        self.assertEqual(self.prospect.last_name, "will")
        self.assertEqual(self.prospect.email, "john.will@email.com")
        self.assertEqual(self.prospect.title, "Head of Sales")
        self.assertEqual(self.prospect.industry, "IT")
        self.assertEqual(self.prospect.country, "Germany")
        # Assert that created_on and updated_at are truly time attributes
        self.assertIsInstance(self.prospect.created_on, datetime)
        self.assertIsInstance(self.prospect_b.updated_at, datetime)
        # Assert that user to prospect relationship is one
        # to multiple
        self.assertEqual(self.prospect.owner, self.user)
        self.assertEqual(self.prospect_b.owner, self.user)
        # Test class Meta ordering
        self.assertEqual(Prospect._meta.ordering, ["company"])
        # Assert that the string method returns the company name
        self.assertEqual(
            str(Prospect(company="A GmbH")),
            self.prospect.company)

    def test_lower_case_converter(self):
        self.user = User.objects.create_user(
            username="TeamUser",
            email="team.user@email.com",
        )
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
        company_upper = UpperCaseConverter().get_prep_value(
            self.prospect.company
            )
        # Assert that UpperCaseConverter converts the company
        # name to upper case
        assert company_upper != self.prospect.company
