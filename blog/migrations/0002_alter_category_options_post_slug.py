# Generated by Django 5.1.3 on 2024-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
