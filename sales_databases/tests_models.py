from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Account, Product


# Create your tests here.

class SuperUserModelTest(TestCase):
    """
    Test Django Superuser model
    """

    def test_create_superuser(self):
        # Create an instance of superuser class
        user = User.objects.create_superuser(
            username="AdminUser",
            password="anything12#",
            email="super.user@email.com",
        )
        # Assert that each attribute is correctly defined
        self.assertEqual(user.username, "AdminUser")
        self.assertIsNotNone(user.password, "anything12#")
        self.assertEqual(user.email, "super.user@email.com")


class UserModelTest(TestCase):
    """
    Test Django user model
    """

    def test_create_user(self):
        user = User.objects.create_user(
            username="TeamUser",
            password="TeamUserPassWord",
            email="team.user@email.com",
        )
        self.assertEqual(user.username, "TeamUser")
        self.assertIsNotNone(user.password, "TeamUserPassWord")
        self.assertEqual(user.email, "team.user@email.com")


class AccountModelTest(TestCase):
    """
    Test Account Model
    """

    def test_create_account(self):
        """
        Create User instance and two Account instances
        """

        self.user = User.objects.create_user(
            username="TeamUser",
            password="TeamUserPassWord",
            email="team.user@email.com",
        )
        self.account = Account.objects.create(
            first_name="john",
            last_name="will",
            email="john.will@email.com",
            job_title="Head of Sales",
            company="A GmbH",
            industry="IT",
            country="Germany",
            account_owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )
        self.account_b = Account.objects.create(
            first_name="john",
            last_name="shall",
            email="john.shall@email.com",
            job_title="Sales Manager",
            company="B GmbH",
            industry="IT",
            country="Germany",
            account_owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now()
        )
        # Assert that each attribute is accurately defined in
        # the Account model
        self.assertEqual(self.account.first_name, "john")
        self.assertEqual(self.account.last_name, "will")
        self.assertEqual(self.account.email, "john.will@email.com")
        self.assertEqual(self.account.job_title, "Head of Sales")
        self.assertEqual(self.account.company, "A GmbH")
        self.assertEqual(self.account.industry, "IT")
        self.assertEqual(self.account.country, "Germany")
        # Assert that created_on and updated_at are truly time attributes
        self.assertIsInstance(self.account.created_on, datetime)
        self.assertIsInstance(self.account_b.updated_at, datetime)
        # Assert that user to account relationship is one
        # to multiple
        self.assertEqual(self.account.account_owner, self.user)
        self.assertEqual(self.account_b.account_owner, self.user)
        # Test class Meta ordering
        self.assertEqual(Account._meta.ordering, ["company"])
        # Assert that the string method returns the company name
        self.assertEqual(
            str(Account(company="A GmbH")),
            self.account.company)


class ProductModelTest(TestCase):
    """
    Test the Product Model
    """

    def test_create_product(self):
        """
        Create User instance and two Product instances
        """
        self.user = User.objects.create_user(
            username="TeamUser",
            password="TeamUserPassWord",
            email="team.user@email.com",
        )
        self.product = Product.objects.create(
            product_name="Product A",
            price=50000,
            currency="USD",
            sales_manager=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )

        self.product_b = Product.objects.create(
            product_name="Product B",
            price=25000,
            currency="EUR",
            sales_manager=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )

        # Assert that each attribute is accurately defined in
        # the Account model
        self.assertEqual(self.product.product_name, "Product A")
        self.assertEqual(self.product.price, 50000)
        self.assertEqual(self.product.currency, "USD")
        self.assertEqual(self.product.sales_manager, self.user)
        self.assertIsInstance(self.product.created_on, datetime)
        self.assertIsInstance(self.product.updated_at, datetime)
        # Assert that User to Product relationship is one
        # to multiple
        self.assertEqual(self.product.sales_manager, self.user)
        self.assertEqual(self.product_b.sales_manager, self.user)
        # Test class Meta ordering
        self.assertEqual(Product._meta.ordering, ["product_name"])
        # Assert that string method returns the product name
        self.assertEqual(
            str(Product(product_name="Product A")),
            self.product.product_name)
