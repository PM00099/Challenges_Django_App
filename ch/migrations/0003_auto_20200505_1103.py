# Generated by Django 2.2.10 on 2020-05-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch', '0002_challenges_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='pic',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]