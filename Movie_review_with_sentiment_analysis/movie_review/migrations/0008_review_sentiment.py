# Generated by Django 5.1.5 on 2025-03-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentiment',
            field=models.IntegerField(default=0),
        ),
    ]
