# Generated by Django 4.0.5 on 2022-07-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_category_slug_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=25),
        ),
    ]
