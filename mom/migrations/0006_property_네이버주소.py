# Generated by Django 4.0.3 on 2024-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom', '0005_delete_image_property_강력추천_property_급매_property_신축_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='네이버주소',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
