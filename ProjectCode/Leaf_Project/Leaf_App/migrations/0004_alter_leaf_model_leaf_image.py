# Generated by Django 4.0.5 on 2022-06-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leaf_App', '0003_remove_leaf_model_leaf_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf_model',
            name='leaf_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Leaf_App/Images'),
        ),
    ]
