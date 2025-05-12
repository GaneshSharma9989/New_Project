from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.show_time, name='show_time'),
]
