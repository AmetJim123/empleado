# Generated by Django 4.0.6 on 2022-08-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_alter_empleado_options_empleado_nombre_completo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='trabajo',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'ABOGADO'), ('4', 'INGENIERO'), ('5', 'COMUNITY MANAGER'), ('6', 'Otro')], max_length=50, verbose_name='Trabajo'),
        ),
    ]
