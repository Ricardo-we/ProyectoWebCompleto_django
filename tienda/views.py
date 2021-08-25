from django.shortcuts import render
from tienda.models import Tienda, ComprasRealizadas
# Create your views here.

def tienda(request):
    tiendaDb = Tienda.objects.all()
    
    tienda_dic = {'tienda_data': tiendaDb,}
    
    return render(request, 'tienda/tienda.html',tienda_dic)

def comprar(request, price, product, description):
    if request.method == "POST":
        email = request.POST['email']
        num_tarjeta = request.POST["numTarjeta"]
        cvc = request.POST["cvc"]
        caducidad = request.POST["caducidad"]

        guardar_compra = ComprasRealizadas(price=price, product=product, email=email, num_tarjeta=num_tarjeta, cvc=cvc,
        caducidad=caducidad)
        guardar_compra.save()

    product_data = {'price':price, 'product':product, 'description':description}
    return render(request, 'tienda/comprar.html' , product_data)

def compra_exitosa(request):
    return render(request, 'tienda/compra_exitosa.html', {}) 
