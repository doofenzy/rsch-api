# Generated by Django 5.1.7 on 2025-03-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_authors_user_alter_reviews_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
