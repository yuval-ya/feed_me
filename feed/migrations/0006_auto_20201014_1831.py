# Generated by Django 3.1.2 on 2020-10-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20201014_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='status',
            field=models.CharField(choices=[('liked', 'liked'), ('unliked', 'unliked')], max_length=8),
        ),
    ]
