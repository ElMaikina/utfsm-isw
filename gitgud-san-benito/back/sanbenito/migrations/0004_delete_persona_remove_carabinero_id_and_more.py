# Generated by Django 4.2.6 on 2023-10-24 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sanbenito', '0003_alter_persona_rut'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.RemoveField(
            model_name='carabinero',
            name='id',
        ),
        migrations.RemoveField(
            model_name='infractor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='inspector',
            name='id',
        ),
        migrations.RemoveField(
            model_name='juez',
            name='id',
        ),
        migrations.AddField(
            model_name='carabinero',
            name='apellidos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carabinero',
            name='fecha_de_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='carabinero',
            name='nombres',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carabinero',
            name='rut',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='infractor',
            name='apellidos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infractor',
            name='fecha_de_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='infractor',
            name='nombres',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infractor',
            name='rut',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='inspector',
            name='apellidos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='inspector',
            name='fecha_de_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inspector',
            name='nombres',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='inspector',
            name='rut',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='juez',
            name='apellidos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='juez',
            name='fecha_de_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='juez',
            name='nombres',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='juez',
            name='rut',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]