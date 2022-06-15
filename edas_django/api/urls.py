from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_rawquestion),
    path('add', views.add_rawquestion),
    
]
