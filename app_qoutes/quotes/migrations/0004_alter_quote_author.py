# Generated by Django 5.0.6 on 2024-05-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_alter_quote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
