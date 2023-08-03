from django import forms
from . models import User

class CustomUserForm(forms.ModelForm):
    phone=forms.CharField()

    class Meta:
        model = User
        fields = ['username','password','email','phone']