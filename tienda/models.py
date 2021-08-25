from django.db import models

# Create your models here.

class Tienda(models.Model):
    product = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='tienda')
    price = models.IntegerField()

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tienda"

    def __str__(self):
        return self.product

class ComprasRealizadas(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    email = models.CharField(max_length=200)
    num_tarjeta = models.CharField(max_length=20)
    cvc = models.CharField(max_length=3)
    caducidad = models.DateField()

    def __str__(self):
        return self.caducidad