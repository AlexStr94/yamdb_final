# Generated by Django 2.2.16 on 2022-03-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
