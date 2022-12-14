# Generated by Django 4.1.3 on 2022-12-01 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=150)),
                ('movie', models.CharField(max_length=150)),
                ('date', models.DateField(max_length=10)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_res', to='tickets.guest')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_res', to='tickets.movie')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
