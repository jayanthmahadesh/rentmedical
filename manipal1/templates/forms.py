from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ..models import ord

class createuserform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"email"}))
    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class orderform(forms.ModelForm):
    class Meta:
        model= ord
        fields= ['username','productname','email','quantity','userid']