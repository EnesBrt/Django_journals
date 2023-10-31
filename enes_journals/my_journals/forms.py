from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='nom et prénom', max_length=100)
    subject = forms.CharField(label='Objet', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    
    
