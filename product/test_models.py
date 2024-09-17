from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Product
from prospect.models import UpperCaseConverter

# Create your tests here.


class ProductModelTest(TestCase):
    """
    Test the Product Model
    """

    def setUp(self):
        """
        Create User instance and two Product instances
        """
        self.user = User.objects.create_user(
            username="TeamUser",
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

    def test_create_product(self):
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

    def test_meta_ordering_method(self):
        # Test class Meta ordering
        self.assertEqual(Product._meta.ordering, ["name"])

    def test_str_method(self):
        # Assert that string method returns the product name
        self.assertEqual(
            str(Product(name="Product A")),
            self.product.name)

    def test_product_price_method(self):
        price = self.product.product_price
        self.assertEqual(price, str(self.product.price) +
                         ' ' + self.product.currency)

    def test_lower_case_converter(self):
        # Test UpperCaseConverter Class on product object
        name_upper = UpperCaseConverter().get_prep_value(
            self.product.name
        )
        assert name_upper != self.product.name
