# Generated by Django 4.0.6 on 2022-08-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0005_alter_departamento_options_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]