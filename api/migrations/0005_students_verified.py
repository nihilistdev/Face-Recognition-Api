# Generated by Django 4.0.4 on 2022-05-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_students_field_of_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]