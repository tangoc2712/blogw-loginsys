from django import forms
from accounts.models import User
from .models import SignVideoUpload



class ContributeRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("fullname", "phone", "facebook")
    