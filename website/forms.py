from django import forms
from website.models import Contact

class ContactForm(forms.ModelForm):

    class Meta: 
        model = Contact
        fields = ['name', 'email', 'message']
        #'__all__' - #['name','email'] - #exclude = ['name']


