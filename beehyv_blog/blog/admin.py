from django.contrib import admin
from models import *

# Register your models here.
class adminUser(admin.ModelAdmin):
    model = User_record
    
class adminBlog(admin.ModelAdmin):
    model = BlogPost_record
    
class adminTag(admin.ModelAdmin):
    model = Tags_list

admin.site.register(User_record, adminUser)
admin.site.register(BlogPost_record, adminBlog)
admin.site.register(Tags_list, adminTag)