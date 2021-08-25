from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('comprar/<int:price>/<str:product>/<str:description>', views.comprar, name="Comprar"),
    path('compra_exitosa/', views.compra_exitosa, name="Compra_exitosa"),
]

