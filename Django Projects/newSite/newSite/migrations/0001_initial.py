# Generated by Django 2.1.7 on 2019-03-19 17:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCliente', models.IntegerField()),
                ('endereco', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('produto', models.CharField(max_length=255)),
                ('flag_atendido', models.BooleanField(default=False)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
