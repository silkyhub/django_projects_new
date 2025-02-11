from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'dtl'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dtl/index.html')),
    path('bottles', views.bottles, name="bottles"),
    path('bottles/<str:drink>', views.bottles, name="bottles_drink"),
    path(
        'bottles/<str:drink>/<int:num_bottles>',
        views.bottles,
        name="bottles_drink_num_bottles",
    ),
]    
