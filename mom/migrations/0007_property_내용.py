# Generated by Django 4.0.3 on 2024-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom', '0006_property_네이버주소'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='내용',
            field=models.TextField(blank=True),
        ),
    ]
