# Generated by Django 3.2.19 on 2023-05-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_massage_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='family_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
