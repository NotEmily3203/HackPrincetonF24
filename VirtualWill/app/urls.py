from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("creator", views.creatorForm, name="creator"),
    path("beneficiary", views.beneficiaryForm, name="beneficiary"),
    path("assignee", views.assigneeForm, name="assignee")
]