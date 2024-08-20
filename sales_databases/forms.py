from .models import Prospect
from django import forms


class ProspectForm(forms.ModelForm):

    class Meta:
        model = Prospect
        fields = ['company',
                  'first_name',
                  'last_name',
                  'email',
                  'title',
                  'industry',
                  'country',
                  ]
