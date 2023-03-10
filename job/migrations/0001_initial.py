# Generated by Django 4.1.7 on 2023-03-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pay', models.PositiveIntegerField()),
                ('required_skills', models.TextField()),
                ('status', models.CharField(choices=[('Hiring', 'Hiring'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Payment', 'Payment'), ('Complete', 'Complete')], default='Hiring', max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='users.users')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_provider', to='users.users', to_field='email')),
            ],
        ),
    ]
