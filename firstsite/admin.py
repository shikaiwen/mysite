from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import HeaderLink
from .models import Post

admin.site.register(HeaderLink)
admin.site.register(Post)
