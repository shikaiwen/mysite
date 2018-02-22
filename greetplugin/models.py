from django.db import models

# Create your models here.
from django.db import models
from cms.constants import PAGE_USERNAME_MAX_LENGTH
# from cms.models.pluginmodel import CMSPlugin
# import cms.models.fields
# class Hello(CMSPlugin):
#     guest_name = models.CharField(max_length=50, default='Guest')
#     haha = cms.models.fields.PageField

class HeaderLink(models.Model):
    name = models.CharField(max_length=30)
    