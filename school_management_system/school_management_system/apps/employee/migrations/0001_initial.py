# Generated by Django 4.1 on 2023-02-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_id', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=150)),
                ('contact_no', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.TextField(default=True)),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
    ]
