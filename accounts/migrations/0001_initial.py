# Generated by Django 4.1.4 on 2022-12-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('pubg_id', models.CharField(blank=True, max_length=11)),
                ('pubg_name', models.CharField(blank=True, max_length=20)),
                ('user', models.CharField(default='', max_length=50)),
            ],
        ),
    ]