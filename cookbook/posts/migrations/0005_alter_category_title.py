# Generated by Django 3.2 on 2022-08-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220812_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=40, unique=True, verbose_name='Наименование'),
        ),
    ]