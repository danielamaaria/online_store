# Generated by Django 3.1.6 on 2021-03-15 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cart_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]