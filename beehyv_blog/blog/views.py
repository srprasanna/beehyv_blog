from django.shortcuts import render
from .models import *
from blog.forms import RegistrationForm
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.core.context_processors import csrf
from django.template import RequestContext
from blog.forms import BlogEntryForm
from django.views.generic import ListView, DetailView
 
#def index(request):
#     
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponse("The password is valid, but the account has been disabled!")
#         else:
#             # the authentication system was unable to verify the username and password
#             return HttpResponse("The username and password were incorrect.")
#         
#     else:
#         #return render_to_response('login.html', {} , context)
#         return render_to_response('home.html',{'full_name':request.user.username},context_instance=RequestContext(request))
#   

# def create_regn_form(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             return HttpResponseRedirect('/success/')
#        
#      else:        
#          form = RegistrationForm()
#          
#      args={}
#      args.update(csrf(request))
#      args['form']=RegistrationForm
#     return ('registet.html',args)
#     #return HttpResponse('{{ form.as_p }}',c)

#def user_login(request):
#     context = RequestContext(request)
#     
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponse("The password is valid, but the account has been disabled!")
#         else:
#             # the authentication system was unable to verify the username and password
#             return HttpResponse("The username and password were incorrect.")
#     
#     else:
#         return render_to_response('login.html', {} , context)

def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/success/')
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("The password is valid, but the account has been disabled!<a href='/'> Home page</a>")
        else:
            # the authentication system was unable to verify the username and password
            return HttpResponse("Invalid entry<a href='/'> Home page</a>")
        
    else:
        #return render_to_response('login.html', {} , context)
        form = RegistrationForm()
        args={}
        args.update(csrf(request))
        args['form']=RegistrationForm
        args['full_name']=request.user.username
        return render_to_response('home.html',args,context_instance=RequestContext(request))
 
def create_blog(request):
    if request.method=='POST':
#        profile=User_record.objects.get(username=request.user.username).user_id
        form=BlogEntryForm(request.POST)
        if form.is_valid():
            form.save(User_record.objects.get(username=request.user.username))
            return HttpResponseRedirect('/')
    args={}
    args.update(csrf(request))
    args['form']=BlogEntryForm      
    return render_to_response('create_post.html',args )

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')
    
def success(request):
    return HttpResponse("Thank you.<a href='/'> Home page</a>")


# def home_page(request):
#     home_page = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
#     template_name = "home_page.html"
#     context = {
#         "home_page": home_page
#     }
#     return render(request, template_name, context)

# class HomePage(ListView):
#     model=Tags_list,
#     #queryset=Tags_list.objects.filter(parent_id = 0 , root_id = 0),
#     context_object_name="tags",
#     template_name = "home_page.html"
#     #context_object_name="home_list",
#     def get_context_data(self, **kwargs):
#         context = super(HomePage, self).get_context_data(**kwargs)
#         context['recent_blog'] = BlogPost_record.objects.filter(blog_post_id = (Blog_tags.objects.get(tag_id = 'tag_id')).blog_post_id ).order_by('-created_date_time')[:1]
#         return context
  
# class CategoryView(DetailView): # use detail view
#     model=BlogPost_record,
#     paginate_by='5',
#     queryset=BlogPost_record.objects.filter(blog_post_id = (Blog_tags.objects.get(tag_id = 'tag_id')).blog_post_id ),
# #     def get_context_data(self, **kwargs):
# #         context = super(CategoryView, self).get_context_data(**kwargs)
# #         context['blogs'] = BlogPost_record.objects.filter(blog_post_id = (Blog_tags.objects.get(tag_id = 'tag_id')).blog_post_id ).order_by('-created_date_time')  # 'tag_id' ???
# #         return context
#     context_object_name="category_view",
#     template_name = "category_view.html"
#  
# class BlogDetail(DetailView):
#     model = BlogPost_record
#     template_name = "post_detail.html"
#     context_object_name="detail_view",
#     queryset=BlogPost_record.objects.all()  # need to add filter separately ??
#  
#  
# # def blog_detail(request, blog_post_id, *args, **kwargs):
# #     post = BlogPost_record.objects.get(blog_post_id = blog_post_id, visibility=True)
# #     template_name = "post_detail.html"
# # 
# #     context = {
# #         "post": post
# #     }
# # 
# #     return render(request, template_name, context)
#  

# def user_create(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#                 # save the model to database, directly from the form:
#                 form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
#                 return HttpResponseRedirect('/success/')
#     else:        
#         form = RegistrationForm()
#     c = { 'form' : form }
#     return render_to_response('registration.html', c)
  
# def user_login(request):
#     if request.method=='POST':
#         username=request.POST.get('Username')
#         password=request.POST.get('Password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return render_to_response()
#             else:
#                 print("The password is valid, but the account has been disabled!")
#         else:
#             # the authentication system was unable to verify the username and password
#             print("The username and password were incorrect.")
#  
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.

def user_home_page(request):
    user_home_page = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
    template_name = "user_home_page.html"
    context = {
        "user_home_page": user_home_page
    }
    return render(request, template_name, context)
 
def my_account( request, *args, **kwargs):
    my_account = User_record.objects.all()
    template_name = "my_account.html"
    context = {
        "my_account": my_account
    }
    return render(request, template_name, context)
 
def edit_account():
    pass
 
def my_posts( request, user_id,  *args, **kwargs):
    my_posts = BlogPost_record.objects.filter(user_id = user_id)
    template_name = "my_posts.html"
    context = {
        "my_posts": my_posts
    }
    return render(request, template_name, context)    
 
#my_post_detail view, from detail view of category list
 
def edit_post():
    pass
 
# def blog_post(self, request, *args, **kwargs):
#     post_list = BlogPost_record.objects.filter(visibility=True).order_by('-created_date_time')[:5]
#     template_name = "post_list.html"
# 
#     context = {
#         "post_list": post_list
#     }
# 
#     return render(request, template_name, context)



