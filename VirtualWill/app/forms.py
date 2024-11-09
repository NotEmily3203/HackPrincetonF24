from django import forms
from app.models import Creator, Beneficiary, Assignee

class CreatorForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ["owner","owner_wallet","beneficiary","beneficiary_wallet","assets"]

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ["ifps_hash"]

class AssigneeForm(forms.ModelForm):
    class Meta:
        model = Assignee
        fields = ["oracle"]