# Generated by Django 2.1.3 on 2019-05-01 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0006_auto_20190501_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
