# Generated by Django 3.2.5 on 2021-08-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210819_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('image1', models.ImageField(upload_to='blog')),
                ('content2', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
