# Generated by Django 3.2.16 on 2023-10-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_journals', '0003_rename_title_articles_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]