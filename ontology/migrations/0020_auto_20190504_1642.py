# Generated by Django 2.1.3 on 2019-05-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0019_auto_20190504_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='Password',
            field=models.CharField(max_length=10),
        ),
    ]