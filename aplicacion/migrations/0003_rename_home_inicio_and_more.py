# Generated by Django 4.2.3 on 2023-07-27 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_nosotros_servicios_rename_profesor_clientes_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home',
            new_name='Inicio',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='apellido',
            new_name='servicio_contratado',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='email',
        ),
    ]
