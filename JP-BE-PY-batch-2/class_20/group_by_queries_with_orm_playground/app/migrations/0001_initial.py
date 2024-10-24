# Generated by Django 4.2.7 on 2024-10-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('salary', models.FloatField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('sales_amount', models.FloatField()),
            ],
            options={
                'db_table': 'sales',
                'managed': False,
            },
        ),
    ]