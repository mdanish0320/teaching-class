# Generated by Django 4.2.7 on 2024-10-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mvs', '0003_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_mvs.category'),
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ManyToManyField(db_column='supplier_id', related_name='products', to='app_mvs.supplier'),
        ),
    ]