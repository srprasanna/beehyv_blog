from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class User_record(User):
    user_id=models.AutoField(primary_key=True)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50, blank=True)
#     username=models.CharField(max_length=50, unique=True)
#     password=models.CharField(max_length=50)
#     email=models.EmailField(unique=True, max_length=50)
    mobile=models.CharField(max_length=10, unique=True)
    designation=models.CharField(max_length=50)
#     created_date_time=models.DateTimeField(auto_now_add=True, editable=False)
#     last_login=models.DateTimeField(auto_now=True, editable=False)
#     is_active=models.BooleanField(default=False)
    is_email_verified=models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name+' '+self.last_name
#     def save(self, *args, **kwargs):
#         super(User_record, self).save(*args, **kwargs)

class BlogPost_record(models.Model):
    blog_post_id=models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User_record)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=50000)
    created_date_time=models.DateTimeField(auto_now_add=True)
    total_views=models.IntegerField(default=0)
    visibility=models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True, default='', unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost_record, self).save(*args, **kwargs)


class Comment_record(models.Model):
    comment_id=models.AutoField(primary_key=True)
    blog_post_id=models.ForeignKey(BlogPost_record)
    user_id=models.ForeignKey(User_record)
    created_date_time=models.DateTimeField(auto_now_add=True, editable=False)
    comment=models.CharField(max_length=50000)
    visibility=models.BooleanField(default=True)

    def __unicode__(self):
        return self.comment
    def save(self, *args, **kwargs):
        super(Comment_record, self).save(*args, **kwargs)

class Tags_list(models.Model):
    tag_id=models.AutoField(primary_key=True)
    tag_name=models.CharField(max_length=50)
    user_id =models.ForeignKey(User_record)
    created_date_time=models.DateTimeField(auto_now_add=True, editable=False)
    parent_id=models.IntegerField()
    root_id=models.IntegerField()

    def __unicode__(self):
        return self.tag_name
    def save(self, *args, **kwargs):
        super(Tags_list, self).save(*args, **kwargs)

class User_tags(models.Model):
    user_id = models.ForeignKey(User_record)
    tag_id=models.ForeignKey(Tags_list)

    def __unicode__(self):
        pass
    def save(self, *args, **kwargs):
        super(User_tags, self).save(*args, **kwargs)

class Blog_tags(models.Model):
    blog_post_id=models.ForeignKey(BlogPost_record)
    tag_id=models.ForeignKey(Tags_list)

    def __unicode__(self):
        pass
    def save(self, *args, **kwargs):
        super(Blog_tags, self).save(*args, **kwargs)

class Liked_post(models.Model):
    blog_post_id=models.ForeignKey(BlogPost_record)
    user_id = models.ForeignKey(User_record)

    def __unicode__(self):
        pass
    def save(self, *args, **kwargs):
        super(Liked_post, self).save(*args, **kwargs)


