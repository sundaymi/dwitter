# import email
from django import forms
from . models import Dweet
from django.core import validators

class DweetForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Dweet something...", "class": "form-control"}), label="", )
    
    class Meta:
        model = Dweet
        exclude = ("user", ) 
        

class SignUpForm(forms.Form):
    GENDERS = (('F','Female'), ('M','Male'),('NB', 'NonBinary'))
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.ChoiceField(label="F for female, M for male, NB for non binary", widget=forms.RadioSelect, choices=GENDERS)
    # We should use a validator to make sure 
    # the user enters a valid number format
    phone_number = forms.CharField(label='Phone',required=False)
    about_you = forms.CharField(widget=forms.Textarea(),required=False)
    

class LoginForm(forms.Form):
    email_login = forms.EmailField()
    password_login = forms.CharField(widget=forms.PasswordInput())
    
    
        
    