# Generated by Django 4.2.3 on 2023-07-19 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart_app.cart_item'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=5),
            preserve_default=False,
        ),
    ]