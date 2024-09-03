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
        blank=False,
        null=False,
    )
    note = models.CharField(
        max_length=500,
        default=None,
        null=True,
    )
    PROBABILITY_OPTIONS = [
        (25, '25%'),
        (50, '50%'),
        (75, '75%'),
        (100, '100%'),
    ]
    probability = models.IntegerField(
        choices=PROBABILITY_OPTIONS,
        default=25,
        blank=False,
        null=False,
    )
    STAGE = (
        ('Lead', 'Lead'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Close', 'Close')
    )
    sales_stage = models.CharField(
        max_length=12,
        choices=STAGE,
        default="Lead",
        blank=False,
        null=False,
    )
    is_closed = models.BooleanField(
        default=False
    )
    STATUS_OPTIONS = [
        ('won', 'won'),
        ('lost', 'lost'),
        ('progress', 'progress')
    ]
    status = models.CharField(
        max_length=8,
        choices=STATUS_OPTIONS,
        default='progress',
        blank=False,
        null=False,
    )
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
