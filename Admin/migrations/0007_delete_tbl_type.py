# Generated by Django 5.0.3 on 2024-03-31 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_place'),
        ('Guest', '0002_delete_tbl_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_type',
        ),
    ]
