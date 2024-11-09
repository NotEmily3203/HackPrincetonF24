from django.urls import path
from . import views

urlpatterns=[
    path("", views.userform, name="home") #root of the website
]