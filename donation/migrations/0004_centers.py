# Generated by Django 3.1.5 on 2021-04-30 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20210429_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('center_id', models.AutoField(primary_key=True, serialize=False)),
                ('center_name', models.CharField(max_length=100)),
                ('center_email', models.EmailField(default='', max_length=70)),
                ('center_phone', models.IntegerField()),
                ('category', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]