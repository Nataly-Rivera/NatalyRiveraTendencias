# Generated by Django 5.0.4 on 2024-04-27 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticHelp',
            fields=[
                ('orderId', models.BigIntegerField(primary_key=True, serialize=False)),
                ('itemDiagnostic', models.CharField(max_length=255)),
                ('nameDiagnostic', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('diagnosticCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('requiresSpecialistD', models.BooleanField()),
                ('specialistId', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employees', models.JSONField(default=list)),
                ('patients', models.JSONField(default=list)),
                ('orders', models.JSONField(default=list)),
                ('invoices', models.JSONField(default=list)),
                ('appointments', models.JSONField(default=list)),
                ('medicines', models.JSONField(default=list)),
                ('diagnosticHelp', models.JSONField(default=list)),
                ('procedures', models.JSONField(default=list)),
                ('visitsHistory', models.JSONField(default=dict)),
                ('clinicalHistory', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('patient_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('patient_age', models.IntegerField()),
                ('patient_name', models.CharField(max_length=255)),
                ('doctor_name', models.CharField(max_length=255)),
                ('insurance_company', models.CharField(max_length=255)),
                ('days_validity', models.IntegerField()),
                ('policy_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('orderid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('itemMedicine', models.CharField(max_length=255)),
                ('medicineName', models.CharField(max_length=255)),
                ('medicineDose', models.CharField(max_length=100)),
                ('durationMedication', models.CharField(max_length=100)),
                ('medicineCost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.BigIntegerField()),
                ('doctor_id', models.BigIntegerField()),
                ('date', models.DateField()),
                ('medicines', models.TextField()),
                ('procedure', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('Contactname', models.CharField(max_length=20)),
                ('patientrelationship', models.CharField(max_length=100)),
                ('insuranceCompany', models.CharField(max_length=100)),
                ('policynumber', models.IntegerField()),
                ('statePolicy', models.CharField(max_length=50)),
                ('policyValidity', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('orderId', models.BigIntegerField(primary_key=True, serialize=False)),
                ('itemProcedure', models.CharField(max_length=255)),
                ('nameProcedure', models.CharField(max_length=255)),
                ('numberRepeated', models.IntegerField()),
                ('frequencyRepeated', models.CharField(max_length=100)),
                ('procedureCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('requiresSpecialistP', models.BooleanField()),
                ('specialistId', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAppointment',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('idDoctor', models.BigIntegerField()),
                ('date', models.DateField()),
                ('idPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.patient')),
            ],
        ),
    ]
