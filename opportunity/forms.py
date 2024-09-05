from .models import Opportunity
from django import forms


class OpportunityForm(forms.ModelForm):

    class Meta:
        model = Opportunity
        fields = [
            'name',
            'lead',
            'solution',
            'note',
            'probability',
            'sales_stage',
            'status',
        ]
