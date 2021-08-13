# Generated by Django 3.2.6 on 2021-08-12 11:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=255)),
                ('phone_number', models.CharField(default='no number', max_length=13)),
                ('is_accepted', models.BooleanField(blank=True, default=False)),
                ('time_start', models.TimeField(blank=True, default=datetime.time(12, 0))),
                ('time_end', models.TimeField(blank=True, default=datetime.time(13, 0))),
                ('date', models.DateField(default=datetime.date(2021, 8, 12))),
                ('is_done', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conclusion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False)),
                ('conclusion_desc', models.TextField(blank=True, max_length=510)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.meeting')),
            ],
        ),
    ]
