from django import forms
from django.forms import fields
from .models import User,Accomodation
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm



class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['FirstName','LastName','EmailId','PassWord','Gender','Address','Mobile','Dob']
        labels={'Dob':'Date of Birth (mm/dd/yyyy)',
        'FirstName':'First Name','LastName':'Last Name',
        'EmailId':'Email Id',
        'PassWord':'Password',
        'Mobile':'Mobile No'}
        widgets={'FirstName':forms.TextInput(attrs={'class':'form-control'}),
        'LastName':forms.TextInput(attrs={'class':'form-control'}),
        'EmailId':forms.EmailInput(attrs={'class':'form-control'}),
        'PassWord':forms.PasswordInput(attrs={'class':'form-control'}),
        'Gender':forms.TextInput(attrs={'class':'form-control'}),
        'Address':forms.TextInput(attrs={'class':'form-control'}),
        'Mobile':forms.TextInput(attrs={'class':'form-control'}),
        'Dob':forms.DateTimeInput(attrs={'class':'form-control'})} 
class AccRegistration(forms.ModelForm):
    class Meta:
        model=Accomodation
        fields=['AccName','ManagerName','AccPhoto','AccAddress','Price','Ratings']
        labels={'AccName':'Listing Name',
        'ManagerName':'Manager Name',
        'AccPhoto':'Image of property',
        'AccAddress':'Address'}
        widgets={'AccName':forms.TextInput(attrs={'class':'form-control'}),
        'ManagerName':forms.TextInput(attrs={'class':'form-control'}),
        'AccAddress':forms.TextInput(attrs={'class':'form-control'}),
        'Price':forms.TextInput(attrs={'class':'form-control'}),
        'Ratings':forms.TextInput(attrs={'class':'form-control'})
        }
        
        
        