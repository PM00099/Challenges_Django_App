# Generated by Django 2.2.10 on 2020-05-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch', '0003_auto_20200505_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='pic',
            field=models.URLField(),
        ),
    ]
