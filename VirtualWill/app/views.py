from django.shortcuts import render, HttpResponse, redirect
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
            pdf_link = f"media/user_info_{clean_form['owner']}.pdf"
            #return redirect('/pdf.html/')
            return render(request, "pdf.html", {'pdf_file': pdf_link})
            return redirect('/pdf')
            
    info = Creator.objects.all()
    context['info'] = info
    context["title"] = "creator"
    context['form'] = form
    
    context['pdf'] = pdf_file
    return render(request, "creator.html",context)


def beneficiaryForm(request):
    context={}
    form=BeneficiaryForm()

    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)
        if form.is_valid():
            #do something with the hash
            #put info you wanna display into this dict
            context = { "pee" : "poop"} 
            return render(request, "beneficiarywill.html", context)
            return redirect('/beneficiarywill')

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

from .web3_service import get_contract_balance, get_owner_details, get_beneficiary_details, is_owner_deceased, check_in

# Example view to display contract balance
def contract_status(request):
    contract_balance = get_contract_balance()
    owner_wallet, owner_name = get_owner_details()
    beneficiary_wallet, beneficiary_name = get_beneficiary_details()
    owner_deceased = is_owner_deceased()

    context = {
        'contract_balance': contract_balance,
        'owner_wallet': owner_wallet,
        'owner_name': owner_name,
        'beneficiary_wallet': beneficiary_wallet,
        'beneficiary_name': beneficiary_name,
        'owner_deceased': owner_deceased,
    }

    return render(request, 'contract_status.html', context)

# Example view to handle check-in
def perform_check_in(request):
    account = "0x418A486a51603D8367EcaC11eeDDEFe47dA87E7f"  # Replace with actual account address
    private_key = "0x1bce540a12d41159a0853d97beeae84f8838628307525b82183d3a165ac8ee36"  # Replace with actual private key
    transaction_hash = check_in(account, private_key)
    
    context = {
        'transaction_hash': transaction_hash
    }

    return render(request, 'check_in.html', context)
