'''
Created on 10-Nov-2014

@author: kapil
'''
from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import User_record,Comment_record,BlogPost_record
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User_record
        fields = ['first_name','last_name','username','password1','password2','email','mobile','designation']
        
    
class BlogEntryForm(ModelForm):
#     title=forms.CharField(max_length=200)
#     content=forms.CharField(widget=Textarea)
#     widgets = {
#             'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
#         }
    class Meta:
        model=BlogPost_record
        fields =('title','content',)
        
    def save(self, user):
        uid = super(BlogEntryForm, self).save(commit=False)
        uid.user_id = user
        uid.save()

class Comment(ModelForm):
    class Meta:
        model = Comment_record
        fields = ('comment',)
    

"""class LoginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=20, required=True)
    password=forms.CharField(label='Password',max_length=50,required=True)"""
    