from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'dtl'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dtl/index.html')),
    path('bottles', views.bottles),
]    
