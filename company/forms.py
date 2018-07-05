
from django import forms
from .models import Company

class CompanyEntryForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


