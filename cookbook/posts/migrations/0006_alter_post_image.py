# Generated by Django 3.2 on 2022-08-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]