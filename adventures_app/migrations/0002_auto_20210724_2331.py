# Generated by Django 3.1.7 on 2021-07-25 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventures_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='profile_pic',
            new_name='picture',
        ),
    ]