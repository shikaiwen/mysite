from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import HeaderLink
from .models import Post
from .forms import PostModelForm

class PostAdmin(admin.ModelAdmin):
    list_display = ("title" ,"meta_description","content",)
#     form = PostModelForm

class HeaderLinkAdmin(admin.ModelAdmin):
#     Post.meta_description
#     HeaderLink._meta
    flist = [x.name for x in HeaderLink._meta.get_fields()]
    flist.remove("content")
    list_display = tuple(flist)
#     list_display = [HeaderLink._meta.get_all_field_names()]
#     list_display = ("id" ,"name","url","titletext","detailtext")

admin.site.register(HeaderLink, HeaderLinkAdmin)
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)

