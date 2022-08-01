# Generated by Django 3.2.14 on 2022-08-01 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20220801_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='lesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.period'),
        ),
    ]