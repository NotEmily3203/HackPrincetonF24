from django import forms
from app.models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['owner', 'beneficiary']