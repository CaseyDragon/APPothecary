# Generated by Django 4.1.4 on 2023-01-05 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipemaker', '0002_alter_recipes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='user',
        ),
        migrations.AddField(
            model_name='recipes',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
