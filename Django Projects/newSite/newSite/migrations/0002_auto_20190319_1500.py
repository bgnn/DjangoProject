# Generated by Django 2.1.7 on 2019-03-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newSite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='endereco',
        ),
    ]
