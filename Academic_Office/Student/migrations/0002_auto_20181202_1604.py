# Generated by Django 2.1.3 on 2018-12-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('A_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('A_max_marks', models.CharField(blank=True, max_length=3, null=True)),
                ('A_marks', models.CharField(blank=True, max_length=3, null=True)),
                ('A_weightage', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='C_assignments',
            field=models.ManyToManyField(to='Student.Assignment'),
        ),
    ]
