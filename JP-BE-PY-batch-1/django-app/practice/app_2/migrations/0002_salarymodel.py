# Generated by Django 4.2.7 on 2023-12-14 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_date', models.DateField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_2.employeemodel')),
            ],
        ),
    ]
