from django.shortcuts import render, HttpResponse
from app.models import Creator, Beneficiary, Assignee
from app.forms import CreatorForm, BeneficiaryForm, AssigneeForm


# Create your views here.
#def home(request):
#    return render(request, "home.html")

def home(request):
    return render(request, "home.html")


def creatorForm(request):
    context={}
    form=CreatorForm()
    info = Creator.objects.all()
    context['info'] = info
    context["title"] = "creator"
    context['form'] = form
    return render(request, "creator.html",context)

def beneficiaryForm(request):
    context={}
    form=BeneficiaryForm()
    info = Beneficiary.objects.all()
    context['info'] = info
    context["title"] = "beneficiary"
    context['form'] = form
    return render(request, "beneficiary.html",context)

def assigneeForm(request):
    context={}
    form=AssigneeForm()
    info = Assignee.objects.all()
    context['info'] = info
    context["title"] = "assignee"
    context['form'] = form
    return render(request, "assignee.html",context)