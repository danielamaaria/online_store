# Generated by Django 3.1.6 on 2021-05-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]
