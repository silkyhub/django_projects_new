from django.urls import re_path 
from django.http import HttpResponse
from django.template import engines
from django.template.loader import render_to_string 


DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'},]


def index(request):
    f = open('index2.html', 'r')
    page = f.read()
    f.close()
    return HttpResponse(page)

def about(request):
    title = "Django Tinyapp"
    author = "José Ejemplo"
    f = open('about.html', 'r')
    template = f.read()
    f.close()
    django_engine = engines['django']
    template = django_engine.from_string(template)
    html = template.render({'title': title, 'author': author})
    return HttpResponse(html)

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about/$', about),
]
