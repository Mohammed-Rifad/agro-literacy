# Generated by Django 2.1.3 on 2019-05-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0022_auto_20190504_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='Photo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]