# Generated by Django 5.0.2 on 2024-03-10 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_firstname_contact_full_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignedUser',
        ),
    ]