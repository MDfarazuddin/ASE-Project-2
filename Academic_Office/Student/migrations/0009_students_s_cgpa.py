# Generated by Django 2.1.3 on 2018-12-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_finalgradepolicy_finalmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='S_cgpa',
            field=models.FloatField(default=0),
        ),
    ]
