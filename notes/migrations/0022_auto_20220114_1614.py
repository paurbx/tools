# Generated by Django 3.1.5 on 2022-01-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0021_delete_userpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
