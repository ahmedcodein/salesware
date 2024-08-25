from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Product

# Create your tests here.


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
            name="Product A",
            price=50000,
            currency="USD",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )

        self.product_b = Product.objects.create(
            name="Product B",
            price=25000,
            currency="EUR",
            owner=self.user,
            created_on=datetime.now(),
            updated_at=datetime.now(),
        )

        # Assert that each attribute is accurately defined in
        # the prospect model
        self.assertEqual(self.product.name, "Product A")
        self.assertEqual(self.product.price, 50000)
        self.assertEqual(self.product.currency, "USD")
        self.assertEqual(self.product.owner, self.user)
        self.assertIsInstance(self.product.created_on, datetime)
        self.assertIsInstance(self.product.updated_at, datetime)
        # Assert that User to Product relationship is one
        # to multiple
        self.assertEqual(self.product.owner, self.user)
        self.assertEqual(self.product_b.owner, self.user)
        # Test class Meta ordering
        self.assertEqual(Product._meta.ordering, ["name"])
        # Assert that string method returns the product name
        self.assertEqual(
            str(Product(name="Product A")),
            self.product.name)
