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
    password = forms.CharField(label="Password",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))
    location = forms.CharField(label="Location",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))

    blood_group = forms.CharField(label="Blood Group",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))
    age = forms.CharField(label="Age",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))

    gender = forms.CharField(label="Gender",widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))

    status = forms.CharField(label="Status",widget=forms.TextInput(
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
