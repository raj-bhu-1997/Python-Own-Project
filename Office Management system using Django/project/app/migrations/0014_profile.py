# Generated by Django 3.2.6 on 2021-12-26 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20211219_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.IntegerField(blank=True, null=True)),
                ('user_mail', models.EmailField(max_length=50, null=True)),
                ('user_mail_password', models.CharField(max_length=30)),
                ('manager_mail', models.EmailField(max_length=50, null=True)),
                ('advicer_mail', models.EmailField(max_length=50, null=True)),
                ('amc_department_mail', models.EmailField(max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ownership')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
