# Generated by Django 3.2.6 on 2021-12-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='type_coolant',
            field=models.CharField(blank=True, choices=[('DCA4', 'DCA4'), ('DCA2', 'DCA2'), ('OTHER', 'OTHER'), ('WATER', 'WATER')], default=None, max_length=6, null=True),
        ),
    ]