# Generated by Django 4.2.6 on 2023-10-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanbenito', '0006_alter_evidencia_acusado_alter_evidencia_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidencia',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
        migrations.AddField(
            model_name='evidencia',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
