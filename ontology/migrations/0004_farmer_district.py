# Generated by Django 2.1.3 on 2019-04-26 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0003_auto_20190426_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='District',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ontology.District'),
        ),
    ]
