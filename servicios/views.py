from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    serv_views_args = {'servicios': servicios,}

    return render(request, "servicios/servicios.html", serv_views_args)

