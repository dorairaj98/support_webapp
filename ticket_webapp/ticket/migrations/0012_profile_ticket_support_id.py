# Generated by Django 3.0.2 on 2020-10-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_auto_20201026_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ticket_support_id',
            field=models.IntegerField(null=True),
        ),
    ]
