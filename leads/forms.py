from django import forms
from .models import Lead


class LeadModelForm(forms.ModelForm):
    """Lead ModelForm"""
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class LeadForm(forms.Form):
    """  Lead form """
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0, max_value=100)
