# Generated by Django 3.1.2 on 2020-10-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_channel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('requests_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_response', models.PositiveIntegerField(default=0)),
                ('text_of_response', models.TextField(max_length=256)),
            ],
        ),
    ]
