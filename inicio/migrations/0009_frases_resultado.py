# Generated by Django 3.0.8 on 2020-07-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_frases'),
    ]

    operations = [
        migrations.AddField(
            model_name='frases',
            name='resultado',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
