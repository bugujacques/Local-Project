# Generated by Django 4.2.5 on 2023-10-10 23:05

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
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=100, null=True)),
                ('lastName', models.CharField(blank=True, max_length=100, null=True)),
                ('researcher', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
    ]