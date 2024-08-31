from django.db import models
from django.contrib.auth.models import User
from prospect.models import Prospect
from product.models import Product

# Create your models here.


class Opportunity(models.Model):
    """
    Instantiates a new Opportunity object
    Define the relationship with the User who
    instantiates the Product object
    Define the relationship with prospect and
    and the product the prospect wants to buy
    """

    name = models.CharField(
        max_length=60,
        unique=True,
        default=None,
        null=False,
    )
    lead = models.ForeignKey(
        Prospect,
        on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    solution = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    note = models.CharField(
        max_length=500,
        unique=False,
        default=None,
        null=True,
    )
    probability = models.IntegerField(
        blank=False,
        default=25,
    )
    is_closed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
    )

    @property
    def winning_probability(self):
        return f"{self.probability}%"

    @property
    def estimation(self):
        est_value = f"""
        {self.product.price * (int(self.winning_probability)/100)}
        """
        return est_value
