# Generated by Django 3.0.5 on 2023-06-18 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_course_exam_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='exam_duration',
        ),
    ]
