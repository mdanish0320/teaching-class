# Generated by Django 4.2.7 on 2024-10-19 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_mvs', '0005_alter_product_user_rename_user_product_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_mvs.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(related_name='products', to='app_mvs.supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
