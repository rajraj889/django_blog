# Generated by Django 2.2.1 on 2019-05-15 04:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190514_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(related_name='articles_written', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles_tagged', to='articles.Tag'),
        ),
    ]
