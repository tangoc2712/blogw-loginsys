from django import forms
from accounts.models import User



class ContributeRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("fullname", "phone", "facebook")