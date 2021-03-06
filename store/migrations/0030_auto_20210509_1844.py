# Generated by Django 3.1.6 on 2021-05-09 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0029_auto_20210509_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='books',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
