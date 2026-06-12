from django import forms
from newsportal.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"