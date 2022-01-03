# Generated by Django 4.0 on 2022-01-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster', models.CharField(max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(default='Smartphone', max_length=255)),
            ],
        ),
    ]
