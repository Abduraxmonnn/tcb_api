# Generated by Django 4.1.7 on 2023-03-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_commenthelper_text_en_commenthelper_text_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
