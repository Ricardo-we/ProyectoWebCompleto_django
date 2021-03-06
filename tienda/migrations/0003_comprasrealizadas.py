# Generated by Django 3.2.5 on 2021-08-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20210810_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasRealizadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('num_tarjeta', models.CharField(max_length=20)),
                ('cvc', models.CharField(max_length=3)),
                ('caducidad', models.CharField(max_length=10)),
            ],
        ),
    ]
