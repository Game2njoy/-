# Generated by Django 4.0.3 on 2024-04-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom', '0010_property_지역'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='지역',
            field=models.CharField(max_length=255),
        ),
    ]
