from django import forms


class LeadForm(forms.Form):
    """  Lead form """
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0, max_value=100)
