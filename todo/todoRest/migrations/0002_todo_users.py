# Generated by Django 2.0.3 on 2018-03-30 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoRest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='users',
            field=models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
