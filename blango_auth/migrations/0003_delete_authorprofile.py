# Generated by Django 3.2.6 on 2022-07-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0002_authorprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthorProfile',
        ),
    ]
