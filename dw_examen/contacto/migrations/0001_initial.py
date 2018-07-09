# Generated by Django 2.0.7 on 2018-07-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, height_field='alto_imagen', null=True, upload_to='', width_field='ancho_imagen')),
                ('alto_imagen', models.IntegerField(default=0)),
                ('ancho_imagen', models.IntegerField(default=0)),
            ],
        ),
    ]
