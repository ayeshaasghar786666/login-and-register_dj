from django import forms
from .models import My_Model

class My_Form(forms.ModelForm):
    class Meta:
        model = My_Model
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }