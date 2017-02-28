from django import forms
from .models import MotivationTerm


class MotivationTermForm(forms.ModelForm):
    class Meta:
        model = MotivationTerm
