# Generated by Django 5.2 on 2025-04-20 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
        ('bookapp', '0002_book_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='bookapp.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.cart')),
            ],
        ),
    ]
