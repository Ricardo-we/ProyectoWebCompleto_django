# Generated by Django 3.2.5 on 2021-08-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210821_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
