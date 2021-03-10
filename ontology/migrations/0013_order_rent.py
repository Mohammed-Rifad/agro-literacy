# Generated by Django 2.1.3 on 2019-05-02 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0012_knowledgecenternotification_knowledgecenterservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Total_Amount', models.PositiveIntegerField()),
                ('Type', models.CharField(max_length=50)),
                ('Status', models.CharField(default='Pending', max_length=50)),
                ('Farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontology.Farmer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontology.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_of_Days', models.PositiveIntegerField()),
                ('Total_Amount', models.PositiveIntegerField()),
                ('Status', models.CharField(default='Pending', max_length=50)),
                ('Farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontology.Farmer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontology.Product')),
            ],
        ),
    ]
