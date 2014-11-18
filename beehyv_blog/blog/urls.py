from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$',views.index),
#    url(r'^hello/$',views.index),
#    url(r'^registration_page/$',views.create_regn_form,name='registration'),
    url(r'^success/$',views.success),
#    url(r'^login/$',views.user_login,name='login'),
#    url(r'^loggedin/$',views.index),
    url(r'^logout/$',views.logout_view),
    url(r'^create_post/$',views.create_blog),
#    url(r'^$', views.HomePage.as_view(), name='home_page'),
#        
#     url(r'^(?P<tag_id>\d+)/$', views.CategoryView.as_view(), name='category_view'),
#     # slug pending
#        
#     url(r'^(?P<tag_id>\d+)/(?P<blogPost_id>\d+)/$', views.BlogDetail.as_view(), name='blog-detail'),
#     # slug pending
    
#    url(r'^user_create/$', views.user_create, name='user_create'),    
       
#    url(r'^login/$', views.user_login, name='login'),
      
    url(r'^user/(?P<user_id>\d+)/$', views.user_home_page, name='user_home_page'),
    # auth pending, add slug
      
    url(r'^user/(?P<user_id>\d+)/my-account/$', views.my_account, name='my-account'),
    # slug pending
      
    url(r'^user/(?P<user_id>\d+)/my-account/edit$', views.edit_account, name='edit-account'),
    # slug pending
      
    url(r'^(?P<user_id>\d+)/my-posts/$', views.my_posts, name='my-posts'),
       
#    url(r'^(?P<user_id>\d+)/my-posts/(?P<blogPost_id>\d+)/$', views.BlogDetail.as_view(), name='my-posts-blog-detail'),
       
    url(r'^(?P<user_id>\d+)/my-posts/(?P<blogPost_id>\d+)/edit-post/$', views.edit_post, name='my-posts-blog-detail-edit'),
       
#    url(r'^(?P<user_id>\d+)/my-posts/add-post$', views.add_post, name='add-post'),
       
       
       
    #url(r'^blog_posts/$', views.blog_post, name='blog_post'),
       
    #url(r'^blogposts/(?P<blogPost_id>\d+)/$', views.blog_detail, name='blogdetail'),
)