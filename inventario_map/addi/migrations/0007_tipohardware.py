# Generated by Django 2.1.4 on 2019-01-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addi', '0006_sedes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipohardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_hardware', models.CharField(max_length=50)),
            ],
        ),
    ]
