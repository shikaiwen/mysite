from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from firstsite.models import Post

# Create your views here.]

# {% load i18n %}
# {% trans username %}
# 在根目录下执行 djangoadmin makemessages -l zh_CN

def index(request):
    template = loader.get_template("mycareer/index.html")
    postlist = list(Post.objects.all().filter(appcode="2"))
    context = {
        "postlist":postlist
    }
    return HttpResponse(template.render(context, request))
