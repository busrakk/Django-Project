# Generated by Django 3.0.5 on 2022-07-27 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20220726_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1. Sınıf Güz', '1. Sınıf Güz'), ('1. Sınıf Bahar', '1. Sınıf Bahar'), ('2. Sınıf Güz', '2. Sınıf Güz'), ('2. Sınıf Bahar', '2. Sınıf Bahar'), ('3. Sınıf Güz', '3. Sınıf Güz'), ('3. Sınıf Bahar', '3. Sınıf Bahar'), ('4. Sınıf Güz', '4. Sınıf Güz'), ('4. Sınıf Bahar', '4. Sınıf Bahar')], max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Period'),
        ),
    ]
