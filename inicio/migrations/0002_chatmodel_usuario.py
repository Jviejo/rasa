# Generated by Django 2.2.7 on 2019-11-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmodel',
            name='usuario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]