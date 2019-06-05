# Generated by Django 2.1.5 on 2019-06-05 03:02

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('messages', models.ManyToManyField(related_name='texts', to='accounts.Message')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='useraccount', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
