# Generated by Django 3.0.6 on 2020-05-27 10:17

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
            name='Challenge',
            fields=[
                ('id', models.AutoField(help_text='A challenge ID, automatically generated by Postgres.', primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('WE', 'Weekly'), ('MO', 'Weekly')], default='WE', help_text='The type of challenge this is, either weekly(WE) or monthly(MO).', max_length=2)),
                ('title', models.TextField(help_text='The challenge title.', max_length=25)),
                ('short_desc', models.TextField(help_text='A summary of the full challenge description.', max_length=100)),
                ('description', models.TextField(help_text='A full description of the challenge.', max_length=2000)),
                ('rules', models.TextField(help_text='A set of rules for this challenge.', max_length=512)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('posted', models.BooleanField(default=False)),
                ('posted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(help_text='The challenge author.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
