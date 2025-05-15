from django import forms
from .models import ContactMessage
from .models import enquiry_table

class ContactForm(forms.ModelForm):
    class Meta:
        model = enquiry_table
        fields = ['name', 'email', 'subject', 'message']
