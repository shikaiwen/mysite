from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import HeaderLink
from .models import Post
from firstsite.AddForm import AddForm
# from .models import Hello 

# https://stackoverflow.com/questions/12704539/how-to-present-data-from-django-cms-custom-plugin-in-template
# 参考になる記事

# bootstrap模板下载地址
# https://bootstrapmade.com/
# https://bootstrapmade.com/demo/MeFamily/
# Create your views here.
# 加强admin功能 https://github.com/django-admin-tools/django-admin-tools/ 


# CKeditor安装和使用：https://pypi.python.org/pypi/django-ckeditor/5.4.0#usage
# http://garmoncheg.blogspot.jp/2014/07/django-adding-custom-widget-to-django.html


# グーグルのウェーブサイト翻訳　https://support.google.com/translate/answer/2534601?hl=en

# add textfilter : https://medium.com/@hakibenita/how-to-add-a-text-filter-to-django-admin-5d1db93772d8
# filter: https://github.com/modlinltd/django-advanced-filters
# http://morozov.ca/why-you-should-use-the-django-admin-9-tips.html

# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def index(request):
    template = loader.get_template("firstsite/index.html")
    currlinkitem = HeaderLink.objects.filter(name="home").get()
    postlist = list(Post.objects.all().filter(appcode="1",show="1").order_by("-created_on"))
    context = {
        "currlinkitem":currlinkitem,
        "postlist":postlist
    }
    return HttpResponse(template.render(context, request))


def post(request, postid):
    currlinkitem = HeaderLink.objects.filter(name="About").get()
    post = Post.objects.get(pk=postid)
    context = {
        "currlinkitem":currlinkitem,
        "post":post
    }
    template = loader.get_template("firstsite/post.html")

    return HttpResponse(template.render(context, request))


def about(request):
    currlinkitem = HeaderLink.objects.filter(name="About").get()
    context = {
        "currlinkitem":currlinkitem
    }
    
    template = loader.get_template("firstsite/about.html")

    return HttpResponse(template.render(context, request))

def blog(request):
    template = loader.get_template("firstsite/index.html")
    currlinkitem = HeaderLink.objects.filter(name="Blog").get()
    postlist = list(Post.objects.all())
    
    context = {
        "currlinkitem":currlinkitem,
        "postlist":postlist
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("firstsite/contact.html")
    currlinkitem = HeaderLink.objects.filter(name="Contact").get()
    context = {
        "currlinkitem":currlinkitem
    }
    return HttpResponse(template.render(context, request))

def formtest(request):
    if request.method == "POST":
        form = AddForm(request.POST) 
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b))) 
    else:
        form = AddForm()
    template = loader.get_template("firstsite/form.html")
    context = {"form":form}
    return HttpResponse(template.render(context, request))
