# Generated by Django 3.1.6 on 2021-03-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.publicdomainpictures.net%2Fpictures%2F60000%2Fnahled%2Fopen-book-1378562978Vki.jpg&f=1&nofb=1'),
        ),
    ]
