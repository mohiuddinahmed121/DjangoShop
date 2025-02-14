# Generated by Django 5.1.1 on 2024-10-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('merchant', 'Merchant')], default='customer', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
