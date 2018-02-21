from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Hello 

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    h =  Hello()
    context = {
        "content": "222222222",
        "title":"jia ttt"
    }
    return HttpResponse(template.render(context, request))