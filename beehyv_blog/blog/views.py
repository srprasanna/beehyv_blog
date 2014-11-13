from django.shortcuts import render
from .models import User_record, BlogPost_record
from blog.forms import RegistrationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView, DetailView

def home_page(request):
    home_page = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
    template_name = "home_page.html"

    context = {
        "home_page": home_page
    }

    return render(request, template_name, context)

"""
def user_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
                # save the model to database, directly from the form:
                form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
                return HttpResponseRedirect('/success/')
    else:        
        form = RegistrationForm()
    c = { 'form' : form }
    return render_to_response('registration.html', c)
"""


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response()
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")

def logout_view(request):
    logout(request)
    # Redirect to a success page.


def user_home_page(request):
    user_home_page = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
    template_name = "user_home_page.html"

    context = {
        "user_home_page": user_home_page
    }

    return render(request, template_name, context)

def my_account(self, request, *args, **kwargs):
    my_account = User_record.objects.all()
    template_name = "my_account.html"

    context = {
        "my_account": my_account
    }

    return render(request, template_name, context)
    
    



def my_posts(self, request, *args, **kwargs):
    my_posts = BlogPost_record.objects.filter(user_id = user_id)  # user_id comes from http_address
    template_name = "my_posts.html"

    context = {
        "my_posts": my_posts
    }

    return render(request, template_name, context)    


def blog_post(self, request, *args, **kwargs):
    post_list = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
    template_name = "post_list.html"

    context = {
        "post_list": post_list
    }

    return render(request, template_name, context)


def blog_detail(request, pk, *args, **kwargs):
    post = BlogPost_record.objects.get(pk =pk, visibility=True)
    template_name = "post_detail.html"

    context = {
        "post": post
    }

    return render(request, template_name, context)




