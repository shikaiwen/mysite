from .models import Post 
import sys
import os
def share_vars(request):
    from .models import HeaderLink
    linklist = list(HeaderLink.objects.filter(show=1))
    os.path.basename(__file__)
    
    modulename = __name__.split(".")[0]
    return {
        'linklist': linklist,
        "modulename": modulename,
        "modulename2": "modulename2",
    }