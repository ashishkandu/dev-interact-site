# Generated by Django 4.2.3 on 2023-07-17 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
