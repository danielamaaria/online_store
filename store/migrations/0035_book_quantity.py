# Generated by Django 3.1.6 on 2021-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_remove_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=50),
        ),
    ]
