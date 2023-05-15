# Generated by Django 4.1 on 2023-05-15 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customuser', '0003_address_global_customuserprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('max_seat', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_address', to='customuser.address_global')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_feature', to='event_controller.eventmain')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attenders', to='event_controller.eventmain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_attendant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]