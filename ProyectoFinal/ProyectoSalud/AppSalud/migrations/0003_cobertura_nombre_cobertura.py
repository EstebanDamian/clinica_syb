# Generated by Django 5.1.2 on 2024-10-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSalud', '0002_alter_cobertura_id_obra_social_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobertura',
            name='nombre_cobertura',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
