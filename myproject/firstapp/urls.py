from django.urls import path
from . import views

urlpatterns = [
    path('skill', views.show_name_skills, name='show_name_skillss'),
]
