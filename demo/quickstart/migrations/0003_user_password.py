# Generated by Django 3.1.4 on 2020-12-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20201217_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
