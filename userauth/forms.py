from django import forms
from .models import User_register, UserInfo, Hackathons

# class DevLoginForm(forms.ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ['name', 'company', 'experience', 'job_title', 'state', 'country', 'domain', 'user__email']

# class StudentLoginForm(forms.ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ['name', 'institute', 'branch', 'interested_domains', 'state', 'country', 'user__email', 'interested_domains_to_follow']

class SampleForm(forms.ModelForm):
    class Meta:
        model = Hackathons
        fields = ['author', 'caption', 'posted_location', 'posted_support', 'queries', 'demo_link']