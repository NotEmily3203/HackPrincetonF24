from django.shortcuts import render, HttpResponse
from app.models import UserInfo
from app.forms import UserInfoForm


# Create your views here.
#def home(request):
#    return render(request, "home.html")

def userform(request):
    context={}
    form=UserInfoForm()
    info = UserInfo.objects.all()
    context['info'] = info
    context["title"] = "Home"
    context['form'] = form
    return render(request, "home.html",context)