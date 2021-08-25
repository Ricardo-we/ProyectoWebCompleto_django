from django.shortcuts import render, redirect
from .forms import ContactUs
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

	form = ContactUs()
	alert_msg = None

	if request.method == "POST":
		form = ContactUs(data=request.POST)
		if form.is_valid():	
			nombre = request.POST.get("nombre")
			email = request.POST.get("email")
			contenido = request.POST.get("contenido")

			email_message = EmailMessage(
				"Mensaje desde django Proyecto Web Completo", 
				f"De {nombre} con la direccion {email} \n Mensaje: \n {contenido}",
				"", ["ricardo0406dev@gmail.com"], reply_to=[email]
			)

			try:
				email_message.send()
				alert_msg = "Se ha enviado satisfactoriamente"
			except:
				return redirect("/?novalido")

			

	return render(request, 'contacto/contactos.html', {"formulario": form, "alert_msg": alert_msg})
