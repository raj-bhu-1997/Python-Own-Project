# Generated by Django 3.2.6 on 2021-12-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_ownership_esn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='amc_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='kva',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='visit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
