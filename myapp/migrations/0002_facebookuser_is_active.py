# Generated by Django 3.1 on 2020-08-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
