# Generated by Django 3.1.6 on 2021-02-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210207_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]