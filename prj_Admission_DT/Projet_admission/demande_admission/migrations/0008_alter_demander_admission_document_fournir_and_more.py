# Generated by Django 4.2.6 on 2023-11-15 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demande_admission', '0007_alter_coordonne_bancaire_date_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demander_admission',
            name='Document_Fournir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demande_admission.document_fournir'),
        ),
        migrations.AlterField(
            model_name='demander_admission',
            name='Information_Personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demande_admission.information_personnelle'),
        ),
        migrations.AlterField(
            model_name='demander_admission',
            name='Paiement_Admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demande_admission.paiement'),
        ),
        migrations.AlterField(
            model_name='demander_admission',
            name='ProgrammeTrimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demande_admission.programmetrimestre'),
        ),
    ]
