# Generated by Django 4.2.6 on 2023-11-13 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande_admission', '0005_demander_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_personnelle',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
