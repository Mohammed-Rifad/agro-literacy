# Generated by Django 2.1.3 on 2019-05-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0010_category_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DealerId', models.PositiveIntegerField()),
                ('Notification', models.TextField()),
            ],
        ),
    ]
