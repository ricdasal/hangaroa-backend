# Generated by Django 4.2.11 on 2024-03-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]