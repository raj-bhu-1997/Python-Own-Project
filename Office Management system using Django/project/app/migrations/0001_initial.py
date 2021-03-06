# Generated by Django 3.2.6 on 2021-12-12 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('esn', models.DecimalField(decimal_places=0, max_digits=10)),
                ('model', models.CharField(max_length=10)),
                ('cpcb_norms', models.CharField(choices=[('C1', 'CPCB1'), ('C2', 'CPCB2')], default='C1', max_length=2)),
                ('visit', models.IntegerField()),
                ('kva', models.IntegerField()),
                ('amc_start', models.DateField()),
                ('amc_end', models.DateField()),
                ('contact_person', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=10, null=True)),
                ('mail_id', models.EmailField(blank=True, max_length=50, null=True)),
                ('last_b', models.DateField(blank=True, null=True)),
                ('last_b_hour', models.IntegerField(blank=True, null=True)),
                ('last_c', models.DateField(blank=True, null=True)),
                ('last_c_hour', models.IntegerField(blank=True, null=True)),
                ('last_d', models.DateField(blank=True, null=True)),
                ('last_d_hour', models.IntegerField(blank=True, null=True)),
                ('last_coolant', models.DateField()),
                ('last_coolant_hour', models.IntegerField(blank=True, null=True)),
                ('last_airfilter', models.DateField()),
                ('last_airfilter_hour', models.IntegerField(blank=True, null=True)),
                ('last_battery', models.DateField()),
                ('battery_type', models.CharField(choices=[('CUM', 'CUMMINS'), ('OTH', 'OTHER')], default='CUM', max_length=3)),
                ('last_battery_hour', models.IntegerField(blank=True, null=True)),
                ('genset_type', models.CharField(blank=True, max_length=20, null=True)),
                ('controller_type', models.CharField(blank=True, choices=[('Cluster', 'Cluster'), ('ECP', 'ECP'), ('ECPG', 'ECPG'), ('POWERCOM', 'POWERCOM'), ('PCC0301', 'PCC0301'), ('PCC1301', 'PCC1301'), ('PCC1302', 'PCC1302'), ('PCC2100', 'PCC2100'), ('PCC3100', 'PCC3100'), ('PCC3201', 'PCC3201'), ('PCC3.3', 'PCC3.3'), ('OTHER', 'OTHER')], default=None, max_length=10, null=True)),
                ('type_coolant', models.CharField(blank=True, choices=[('DCA4', 'DCA4'), ('DCA2', 'DCA2')], default=None, max_length=4, null=True)),
                ('equ_model', models.CharField(blank=True, max_length=10, null=True)),
                ('equ_serial', models.CharField(blank=True, max_length=10, null=True)),
                ('last_fueltank_clean', models.DateField(blank=True, null=True)),
                ('last_radiator_clean', models.DateField(blank=True, null=True)),
                ('last_hose_replacement', models.DateField(blank=True, null=True)),
                ('last_plumber_block', models.DateField(blank=True, null=True)),
                ('last_healthcheck', models.DateField(blank=True, null=True)),
                ('last_fiveyearkit', models.DateField(blank=True, null=True)),
                ('recent_hour', models.IntegerField(blank=True, null=True)),
                ('reminder_count_b', models.IntegerField(blank=True, null=True)),
                ('reminder_count_coolant', models.IntegerField(blank=True, null=True)),
                ('reminder_count_battery', models.IntegerField(blank=True, null=True)),
                ('reminder_count_airfilter', models.IntegerField(blank=True, null=True)),
                ('remark_b', models.CharField(blank=True, max_length=50, null=True)),
                ('remark_coolant', models.CharField(blank=True, max_length=50, null=True)),
                ('remark_battery', models.CharField(blank=True, max_length=50, null=True)),
                ('remark_airfilter', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
