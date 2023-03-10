# Generated by Django 4.1.4 on 2022-12-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('country', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pubg_id', models.IntegerField()),
                ('Match_id', models.IntegerField()),
                ('match_name', models.CharField(max_length=20)),
                ('pubg_name', models.CharField(max_length=20)),
                ('kill', models.IntegerField(null=True)),
                ('win', models.CharField(default='', max_length=3)),
                ('Email', models.CharField(default='', max_length=80)),
                ('amount', models.IntegerField(default=0, null=True)),
                ('order_id', models.CharField(default='', max_length=10)),
                ('user_id', models.IntegerField(default=0)),
                ('payment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(max_length=20)),
                ('match_type', models.CharField(max_length=5)),
                ('match_map', models.CharField(max_length=20)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('match_entry', models.IntegerField()),
                ('per_kill_prize', models.IntegerField()),
                ('winner_prize', models.IntegerField()),
                ('match_pics', models.ImageField(default='', upload_to='')),
                ('prize_pool', models.IntegerField(default=0)),
                ('room_id', models.CharField(blank='True', default='', max_length=10)),
                ('room_pass', models.CharField(blank='True', default='', max_length=10)),
            ],
        ),
    ]
