from django import forms
from . models import User

class UserForm(forms.ModelForm):
    name = forms.CharField(label="Donor Name",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))
    email = forms.CharField(label="Email",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))

    class Meta:
        model = User
        fields = [
                'name','email','password','location',
                'blood_group','age','gender','status',
            ]
