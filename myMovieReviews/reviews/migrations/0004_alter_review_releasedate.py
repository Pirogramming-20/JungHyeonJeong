# Generated by Django 5.0.1 on 2024-01-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='releaseDate',
            field=models.DateField(),
        ),
    ]