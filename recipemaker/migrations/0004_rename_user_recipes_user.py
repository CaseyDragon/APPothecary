# Generated by Django 4.1.4 on 2023-01-05 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipemaker', '0003_remove_recipes_user_recipes_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='User',
            new_name='user',
        ),
    ]
