from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index*', views.index, name='index'),
    url(r'^about*', views.about, name='about'),
    url(r'^blog*', views.blog, name='blog'),
    url(r'^contact*', views.contact, name='contact'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^form*', views.formtest, name='formtest'),
    
]