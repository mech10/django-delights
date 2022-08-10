# Generated by Django 4.0.6 on 2022-07-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='price_per_unit',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]