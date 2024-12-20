# Generated by Django 5.1 on 2024-11-23 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choozy', '0009_rename_response_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reslults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restraunt_name', models.CharField(max_length=128)),
                ('image_url', models.TextField()),
                ('menu_url', models.TextField()),
                ('yelp_url', models.TextField()),
                ('phone', models.CharField(max_length=32)),
                ('rating', models.FloatField()),
                ('price', models.CharField(max_length=4)),
                ('categories', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='choozy.room')),
            ],
        ),
    ]
