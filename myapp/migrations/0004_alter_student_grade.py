# Generated by Django 4.0.5 on 2022-07-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_grade_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(blank=True, choices=[('1', '1. grade'), ('2', '2'), ('3', '3'), ('4', '4')], null=True),
        ),
    ]
