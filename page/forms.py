from django import forms
from django.forms import ModelForm

# Create your forms here.

class ContactForm(forms.Form):
	full_name = forms.CharField(label="Full Name" ,max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
	subject = forms.CharField(label="Subject" ,max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
	email_address = forms.EmailField(label="Email Address",max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
	message = forms.CharField(label="Message" ,widget=forms.Textarea(attrs={'class': 'form-control p-4'}), max_length = 2000)
	
