# Generated by Django 3.0.4 on 2020-05-13 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrada.Category'),
        ),
    ]
