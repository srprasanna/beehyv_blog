from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    
    url(r'^$', views.home_page, name='home_page'),
    
    
    
    
    
    url(r'^(?P<user_id>\d+)/$', views.user_home_page, name='user_home_page'),
    # auth pending
    
    url(r'^(?P<user_id>\d+)/my_account/$', views.my_account, name='my_account'),
    
    url(r'^(?P<user_id>\d+)/my_posts/$', views.my_posts, name='my_posts'),
    
    url(r'^blog_posts/$', views.blog_post, name='blog_post'),
    
    url(r'^blog_posts/(?P<blogPost_id>\d+)/$', views.blog_detail, name='blog_detail'),

    url(r'^user_create/$', views.user_create, name='user_create'),
    
    url(r'^user_login/$', views.user_login, name='user_login'),
    
    url(r'^blog_posts/(?P<blogPost_id>\d+)/$', views.blog_detail, name='blog_detail'),

)