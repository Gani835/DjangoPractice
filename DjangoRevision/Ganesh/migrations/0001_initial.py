# Generated by Django 4.1 on 2022-11-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=20)),
                ('EmployeeName', models.CharField(max_length=20)),
                ('EmployeeAge', models.IntegerField()),
            ],
        ),
    ]
