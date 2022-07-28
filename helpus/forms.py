from django import forms
from accounts.models import User



# class ContributeRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("fullname", "phone", "facebook")
    
class ContributeRegisterForm(forms.Form):
    word = forms.CharField()
    file = forms.FileField()