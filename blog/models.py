from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.jpg', '.png']
    if not ext.lower() in valid_ext:
        raise ValidationError('Unsupported file extention')

class UserProfile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    avator = models.FileField(upload_to='files/user_avatar',null=False, blank=False, validators=[validate_file_extention])
    description = models.CharField( max_length=512, null=False, blank=False)

  

class Article(models.Model):
    cover = models.FileField(upload_to='files/article_cover',null=False, blank=False, validators=[validate_file_extention])
    title = models.CharField( max_length=128, null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    
class Category(models.Model):
    cover = models.FileField(upload_to='files/category_cover',null=False, blank=False, validators=[validate_file_extention])
    title = models.CharField( max_length=128, null=False, blank=False)
    
   
    
