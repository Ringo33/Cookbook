# Generated by Django 3.2 on 2022-08-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220811_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=128, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
