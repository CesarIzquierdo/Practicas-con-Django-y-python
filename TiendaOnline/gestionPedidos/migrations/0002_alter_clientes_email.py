# Generated by Django 5.0.1 on 2024-01-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
