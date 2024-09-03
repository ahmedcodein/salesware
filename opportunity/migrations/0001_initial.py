# Generated by Django 5.0.7 on 2024-09-03 22:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('prospect', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60, unique=True)),
                ('note', models.CharField(default=None, max_length=500, null=True)),
                ('probability', models.IntegerField(choices=[(25, '25%'), (50, '50%'), (75, '75%'), (100, '100%')], default=25)),
                ('sales_stage', models.CharField(choices=[('Lead', 'Lead'), ('Proposal', 'Proposal'), ('Negotiation', 'Negotiation'), ('Close', 'Close')], default='Lead', max_length=12)),
                ('is_closed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('won', 'won'), ('lost', 'lost'), ('progress', 'progress')], default='progress', max_length=8)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lead', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='prospect.prospect')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('solution', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
