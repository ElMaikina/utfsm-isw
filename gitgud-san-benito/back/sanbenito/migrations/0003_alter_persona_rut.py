# Generated by Django 4.2.6 on 2023-10-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanbenito', '0002_evidencia_infraccion_infractor_inspector_juez_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]