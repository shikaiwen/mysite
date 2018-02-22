from django.shortcuts import render
from django.utils.translation import ugettext as _

# Create your views here.

def index(request):
	return render(request, "index.html", 
		{
			"text":_("text"),
			"val":_("var")
		}
		)