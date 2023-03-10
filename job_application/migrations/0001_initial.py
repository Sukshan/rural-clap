# Generated by Django 4.1.7 on 2023-03-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
