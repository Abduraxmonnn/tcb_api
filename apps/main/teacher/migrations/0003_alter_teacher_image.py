# Generated by Django 4.1.7 on 2023-03-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_description_en_teacher_description_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Teachers/%Y/%m'),
        ),
    ]
