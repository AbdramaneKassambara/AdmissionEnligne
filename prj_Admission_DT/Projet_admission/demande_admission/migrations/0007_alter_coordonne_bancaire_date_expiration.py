# Generated by Django 4.2.6 on 2023-11-15 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande_admission', '0006_alter_information_personnelle_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordonne_bancaire',
            name='date_expiration',
            field=models.CharField(max_length=10),
        ),
    ]
