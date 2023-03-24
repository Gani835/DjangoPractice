# Generated by Django 4.1 on 2022-11-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ganesh', '0009_vehicle2_rename_custom_customer2_delete_vehic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Customer', models.ManyToManyField(related_name='Vehicle3', to='Ganesh.customer3')),
            ],
        ),
    ]
