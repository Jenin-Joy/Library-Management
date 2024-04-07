# Generated by Django 5.0.3 on 2024-03-31 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0005_initial'),
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_book_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('collected_date', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('returned_date', models.DateField(null=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.tbl_book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
