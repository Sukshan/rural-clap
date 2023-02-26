# Generated by Django 4.1.7 on 2023-02-26 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_provider', '0001_initial'),
        ('job', '0002_job_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('service_provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_provider.service_provider')),
            ],
        ),
    ]
