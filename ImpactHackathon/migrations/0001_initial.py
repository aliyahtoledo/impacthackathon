# Generated by Django 2.1.4 on 2020-08-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropName', models.CharField(max_length=1000)),
                ('orderDate', models.DateField()),
                ('orderType', models.CharField(max_length=1000)),
                ('arrivalDate', models.DateField()),
                ('partnerName', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField(default=0)),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropName', models.CharField(max_length=1000)),
                ('salesDate', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('demand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ImpactHackathon.Demand')),
            ],
        ),
    ]
