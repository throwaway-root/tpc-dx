# Generated by Django 3.0.5 on 2023-06-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_duration',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
