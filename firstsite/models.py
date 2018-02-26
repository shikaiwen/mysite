from django.db import models

# Create your models here.
from django.db import models
# from cms.constants import PAGE_USERNAME_MAX_LENGTH
# from tinymce.models import  HTMLField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class HeaderLink(models.Model):
    
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    
    titletext =  models.CharField(max_length=100,blank=True)
    detailtext =  models.CharField(max_length=100,blank=True)
    
    show = models.BigIntegerField(blank=True,default=1)
    content = RichTextUploadingField(blank=True)
    
    def __str__(self):
        strdata = ""
        namedict = {}
        namelist = HeaderLink._meta.get_fields()
        for i,field in enumerate(namelist):
            namedict[field.attname] = getattr(self, field.attname)
        
        return 'HeaderLink: ' + str(namedict)
    
    def __iter__(self):
        for field_name in self._meta.get_all_field_names():
            value = getattr(self, field_name, None)
            yield (field_name, value)
#         return 'HeaderLink: ' + str(dict(self))
#     content = models.TextField(max_length=3000, blank=True)
#     content = HTMLField()


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    postcode = models.CharField(max_length=100, blank=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
#     content = models.TextField()
#     content = RichTextField()
    content = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='static/blog/uploads/%Y/%m/%d/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    LAN_CHOICES = (
            ("en","English"),
            ("cn","Chinese"),
            ("ja","Japanese"),
        ) 
    
    lantype = models.CharField(default="en",max_length=10,choices= LAN_CHOICES, blank=True)
    
    APP_CHOICES = (
        ("1","mainsite"),
        ("2","mycareer"),
    ) 
    appcode = models.CharField(default="1", max_length=5,choices= APP_CHOICES, blank=True)
#     appcode 
    def __str__(self):
        namedict = {}
        namelist = Post._meta.get_fields()
        for i,field in enumerate(namelist):
            namedict[field.attname] = getattr(self, field.attname)
        
        return 'Post: ' + str(namedict)