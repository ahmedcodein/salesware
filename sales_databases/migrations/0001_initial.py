# Generated by Django 5.0.7 on 2024-07-30 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('GBP', 'GBP')], default='EUR', max_length=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=None, max_length=60, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(default=None, max_length=40)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('title', models.CharField(default=None, max_length=60, null=True)),
                ('industry', models.CharField(default=None, max_length=60)),
                ('country', models.CharField(default=None, max_length=60)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['company'],
            },
        ),
    ]
