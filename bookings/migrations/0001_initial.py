# Generated by Django 5.0.2 on 2024-05-30 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TaxiDetails',
            fields=[
                ('taxi_id', models.AutoField(primary_key=True, serialize=False)),
                ('regisration_number', models.CharField(max_length=15, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentReceipt',
            fields=[
                ('receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.customer')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.taxidetails')),
            ],
        ),
    ]
