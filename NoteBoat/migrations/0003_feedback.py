# Generated by Django 3.0.8 on 2020-08-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteBoat', '0002_userdata_completion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('datetime', models.CharField(max_length=24)),
            ],
        ),
    ]
