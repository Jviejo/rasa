# Generated by Django 2.2.7 on 2019-11-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_auto_20191127_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='texto',
            field=models.CharField(max_length=1000),
        ),
    ]
