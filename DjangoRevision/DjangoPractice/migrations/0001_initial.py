# Generated by Django 4.1 on 2022-11-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsDetailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_ID', models.IntegerField()),
                ('Product_Category', models.CharField(max_length=100)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_Price', models.IntegerField()),
            ],
        ),
    ]
