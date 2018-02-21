from django.db import models

# Create your models here.
from cms.models.pluginmodel import CMSPlugin
from django.db import models
import cms.models.fields

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')
    haha = cms.models.fields.PageField