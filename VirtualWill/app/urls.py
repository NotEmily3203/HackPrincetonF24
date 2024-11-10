from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("creator", views.creatorForm, name="creator"),
    path("beneficiary", views.beneficiaryForm, name="beneficiary"),
    path("assignee", views.assigneeForm, name="assignee")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)