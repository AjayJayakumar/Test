# Generated by Django 4.1.1 on 2022-09-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsnippets',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
