# Generated by Django 5.2 on 2025-04-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]
