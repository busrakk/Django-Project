# Generated by Django 4.0.5 on 2022-07-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='lettergrade',
            field=models.CharField(choices=[('AA', 'AA'), ('BB', 'BB'), ('FF', 'FF')], max_length=2, null=True),
        ),
    ]
