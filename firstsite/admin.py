from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import HeaderLink
from .models import Post
from .forms import PostModelForm

class PostAdmin(admin.ModelAdmin):
    list_display = ("title" ,"meta_description","content",)
    form = PostModelForm
    

admin.site.register(HeaderLink)
admin.site.register(Post)
# admin.site.register(Post, PostAdmin)

