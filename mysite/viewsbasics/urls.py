from django.urls import path
from . import views


appname = 'viewsbasics'
urlpatterns = [
    path('danger', views.danger),
]    
