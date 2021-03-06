# Generated by Django 3.0.8 on 2020-07-09 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20191127_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='chatmodel',
            options={'ordering': ('-fecha',)},
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Cliente')),
            ],
        ),
    ]
