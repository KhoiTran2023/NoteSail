# Generated by Django 3.0.8 on 2020-08-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteBoat', '0004_remove_userdata_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
