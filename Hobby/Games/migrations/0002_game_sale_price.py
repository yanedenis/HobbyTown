# Generated by Django 5.0.4 on 2024-05-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='sale_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
