# Generated by Django 3.1.5 on 2021-04-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_auto_20210429_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='phone',
        ),
        migrations.AddField(
            model_name='donor',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]