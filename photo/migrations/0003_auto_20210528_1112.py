# Generated by Django 3.2.1 on 2021-05-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20210528_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]