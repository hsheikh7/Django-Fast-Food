# Generated by Django 3.2.19 on 2023-05-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20230525_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]