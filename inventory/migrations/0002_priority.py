# Generated by Django 3.2 on 2023-02-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified', models.DateField(auto_now=True, verbose_name='Update Date')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('classification', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=6, verbose_name='Classification')),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
            },
        ),
    ]