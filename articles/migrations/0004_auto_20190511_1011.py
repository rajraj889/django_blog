# Generated by Django 2.2.1 on 2019-05-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190511_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data_created',
            new_name='date_created',
        ),
    ]
