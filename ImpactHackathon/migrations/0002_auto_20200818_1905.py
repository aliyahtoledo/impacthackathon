# Generated by Django 2.1.4 on 2020-08-18 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ImpactHackathon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='demand',
        ),
        migrations.DeleteModel(
            name='Demand',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]