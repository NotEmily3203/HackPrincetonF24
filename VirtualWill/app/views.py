from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.conf import settings
from app.models import Creator, Beneficiary, Assignee
from app.forms import CreatorForm, BeneficiaryForm, AssigneeForm

import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Create your views here.
#def home(request):
#    return render(request, "home.html")

def home(request):
    return render(request, "home.html")


def creatorForm(request):
    context={}
    form=CreatorForm()
    pdf_file=None
    if request.method == 'POST':
        form = CreatorForm(request.POST)
        if form.is_valid():
            clean_form = {
                'owner' : form.cleaned_data['owner'],
                'owner_wallet' : form.cleaned_data['owner_wallet'],
                'beneficiary' : form.cleaned_data['beneficiary'],
                'beneficiary_wallet' : form.cleaned_data['beneficiary_wallet'],
                'assets' : form.cleaned_data['assets']
            }
            pdf_file_path = os.path.join(settings.MEDIA_ROOT, f"user_info_{clean_form['owner']}.pdf")
            
            pdf_file = generate_pdf(clean_form, pdf_file_path)
    info = Creator.objects.all()
    context['info'] = info
    context["title"] = "creator"
    context['form'] = form
    context['pdf'] = pdf_file
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

def generate_pdf(user_info, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Write data to the PDF
    c.drawString(100, height - 100, f"Owner: {user_info['owner']}")
    c.drawString(100, height - 120, f"Owner Wallet: {user_info['owner_wallet']}")
    c.drawString(100, height - 140, f"Beneficiary: {user_info['beneficiary']}")
    c.drawString(100, height - 160, f"Beneficiary Wallet: {user_info['beneficiary_wallet']}")
    c.drawString(100, height - 180, f"Assets: {user_info['assets']}")
    
    
    # Save the PDF
    c.showPage()
    return c.save()