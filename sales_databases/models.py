from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    """
    Instantiates a new Account object
    Define the relationship with the User who
    instantiates the Account object
    """
    company = models.CharField(max_length=60, default=None, null=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, default=None, null=False)
    email = models.EmailField(default=None, null=False)
    job_title = models.CharField(max_length=60, default=None, null=True)
    industry = models.CharField(max_length=60, default=None, null=False)
    country = models.CharField(max_length=60, default=None, null=False)
    account_owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True, null=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=False,
    )

    class Meta:
        """
        Sort the Accounts alphabetically
        """
        ordering = ["company"]

    def __str__(self):
        """
        Returns a the company name string as
        a representation of the Account object
        """
        return self.company


class Product(models.Model):
    """
    Instantiates a new Product object
    Define the relationship with the User who
    instantiates the Product object
    """
    product_name = models.CharField(max_length=60, default=None, null=False)
    price = models.IntegerField(default=None, null=False)
    CURRENCY_OPTIONS = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('GBP', 'GBP')
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_OPTIONS,
        default="EUR",
        )

    sales_manager = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True, null=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=False,
    )

    class Meta:
        """
        Sort the Products alphabetically
        """
        ordering = ["product_name"]

    def product_price(self):
        return f"Product Price {self.currency} {self.price}"

    def __str__(self):
        """
        Returns a the product name string as
        a representation of the Account object
        """
        return self.product_name
