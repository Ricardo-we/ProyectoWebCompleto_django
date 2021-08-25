from django import forms

class ContactUs(forms.Form):
	nombre = forms.CharField(max_length=70, label="Nombre", required=True)
	email = forms.CharField(max_length=70, label="Email", required=True)
	contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
