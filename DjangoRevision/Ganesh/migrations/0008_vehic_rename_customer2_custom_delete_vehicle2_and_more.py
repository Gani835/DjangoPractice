# Generated by Django 4.1 on 2022-11-10 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ganesh', '0007_customer2_alter_vehicle_customer_vehicle2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer2',
            new_name='Custom',
        ),
        migrations.DeleteModel(
            name='Vehicle2',
        ),
        migrations.AddField(
            model_name='vehic',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vehic', to='Ganesh.custom'),
        ),
    ]
