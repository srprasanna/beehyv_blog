'''
Created on 10-Nov-2014

@author: kapil
'''
from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea
from blog.models import User_record

class RegistrationForm(ModelForm):
    class Meta:
        model=User_record
        fields = ['first_name','last_name','username','password','email','mobile','designation']
        
form = RegistrationForm()

regn = User_record.objects.get(pk=1)
form = RegistrationForm(instance=regn)


"""class RegistrationForm(forms.Form):
    first_name=forms.CharField(label='First Name',max_length=20,required=True)
    last_name=forms.CharField(label='Last Name',max_length=20,required=True)
    username=forms.CharField(label='Username',max_length=20, unique=True, required=True)
    password=forms.CharField(label='Password',max_length=50,required=True)
    password1=forms.CharField(label='Verify Password',max_length=50,required=True)
    email=forms.EmailField(unique=True, max_length=50, required=True)
    mobile=forms.CharField(max_length=10, unique=True,required=True)
    designation=forms.CharField(max_length=20,required=True)"""
    
class BlogEntryForm(ModelForm):
    title=forms.CharField(max_length=200)
    content=forms.CharField(widget=Textarea)

class Comment(ModelForm):
    comment=forms.CharField(widget=Textarea)
    

"""class LoginForm(ModelForm):
    username=forms.CharField(label='Username',max_length=20, unique=True, required=True)
    password=forms.CharField(label='Password',max_length=50,required=True)"""
    