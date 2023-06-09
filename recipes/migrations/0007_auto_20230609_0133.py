# Generated by Django 3.2.13 on 2023-06-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving',
            field=models.PositiveIntegerField(null=True),
        ),
    ]