from django import forms
from .models import *


class EmailForm(forms.ModelForm):
    """
    Form for sing_up user
    """
    e_mail = forms.EmailField()

    class Meta:
        model = Email
        fields = '__all__'


class PhoneNumberForm(forms.ModelForm):
    """
    UserUpdateForm for update base django User
    """

    class Meta:
        model = PhoneNumber
        fields = '__all__'
