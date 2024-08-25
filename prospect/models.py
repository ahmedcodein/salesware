from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Prospect(models.Model):
    """
    Instantiates a new Prospect object
    Define the relationship with the User who
    instantiates the Prospect object
    """
    company = models.CharField(
        max_length=60,
        unique=True,
        default=None,
        null=False,
        )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, default=None, null=False)
    email = models.EmailField(default=None, null=False)
    title = models.CharField(max_length=60, default=None, null=True)
    industry = models.CharField(max_length=60, default=None, null=False)
    country = models.CharField(max_length=60, default=None, null=False)
    owner = models.ForeignKey(
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
        Sort the Prospects alphabetically
        """
        ordering = ["company"]

    def __str__(self):
        """
        Returns a the company name string as
        a representation of the Prospect object
        """
        return self.company
