# Generated by Django 3.1.3 on 2021-03-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_auto_20210314_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Room_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]