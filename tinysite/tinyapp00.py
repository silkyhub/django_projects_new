from django.urls import re_path 
from django.http import HttpResponse


ALLOWED_HOSTS = ['*']
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__


def index(request):
    f = open('index.html', 'r')
    page = f.read()
    f.close()
    return HttpResponse(page)


urlpatterns = [
    re_path(r'^$', index),
]
