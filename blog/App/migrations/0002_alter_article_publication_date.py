# Generated by Django 5.0 on 2023-12-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
