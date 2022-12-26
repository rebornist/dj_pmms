# Generated by Django 3.2.13 on 2022-06-08 07:40

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
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('business_amount', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.BooleanField(default=True)),
                ('start_date', models.DateField(blank=True, default='')),
                ('end_date', models.DateField(blank=True, default='')),
                ('implementation_year', models.PositiveSmallIntegerField()),
                ('host_company', models.CharField(blank=True, default='', max_length=50)),
                ('general_manager', models.CharField(blank=True, default='', max_length=50)),
                ('general_manager_phone', models.CharField(blank=True, default='', max_length=50)),
                ('general_manager_email', models.CharField(blank=True, default='', max_length=150)),
                ('host_institution', models.CharField(blank=True, default='', max_length=50)),
                ('host_manager', models.CharField(blank=True, default='', max_length=50)),
                ('host_manager_phone', models.CharField(blank=True, default='', max_length=50)),
                ('host_manager_email', models.CharField(blank=True, default='', max_length=150)),
                ('host_address', models.CharField(blank=True, default='', max_length=255)),
                ('workflow_active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]