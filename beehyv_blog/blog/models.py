from django.db import models
from django.template.defaultfilters import slugify

class User_record(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20, unique=True, editable=False)
    password=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=50, editable=False)
    mobile=models.CharField(max_length=10, unique=True)
    designation=models.CharField(max_length=20)
    created_date_time=models.DateTimeField(auto_now_add=True, editable=False)
    last_login=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name+' '+self.last_name
    def save(self, *args, **kwargs):
        super(User_record, self).save(*args, **kwargs)

class BlogPost_record(models.Model):
    user_id = models.ForeignKey(User_record)
    blogPost_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_date_time=models.DateTimeField(auto_now_add=True)
    total_views=models.IntegerField()
    visibility=models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True, default='')

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
    created_date_time=models.DateTimeField(auto_now_add=True)
    comment=models.TextField()
    visibility=models.BooleanField(default=True)

    def __unicode__(self):
        return self.comment[:10]+'...'
    def save(self, *args, **kwargs):
        super(Comment_record, self).save(*args, **kwargs)

class Tags_list(models.Model):
    tag_id=models.AutoField(primary_key=True)
    tag_name=models.CharField(max_length=50)
    user_id =models.ForeignKey(User_record)
    created_date_time=models.DateTimeField(auto_now_add=True)
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



