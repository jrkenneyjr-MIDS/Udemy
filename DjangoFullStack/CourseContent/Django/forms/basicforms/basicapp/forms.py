from django import forms
from django.core import validators
from basicapp.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email Again!")
    text = forms.CharField(widget=forms.Textarea, required=False)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        botcatcher = all_clean_data['botcatcher']
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
        elif len(botcatcher)>0:
            raise forms.ValidationError("GOTCHA BOT!")
