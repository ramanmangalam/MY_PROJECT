# Generated by Django 5.0.1 on 2024-01-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeApp', '0003_rename_contact_contact1'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_json', models.CharField(max_length=300)),
                ('amount', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('address1', models.TextField(max_length=300)),
                ('address2', models.TextField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('zipcode', models.IntegerField()),
                ('paymentdetails', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='orderupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField()),
                ('update_desc', models.CharField(max_length=300)),
                ('delivered', models.BooleanField()),
                ('timestamp', models.DateField()),
            ],
        ),
    ]