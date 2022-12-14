# Generated by Django 4.0.6 on 2022-07-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['primer_nombre'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='trabajo',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'ABOGADO'), ('4', 'OTRO')], max_length=50, verbose_name='Trabajo'),
        ),
    ]
