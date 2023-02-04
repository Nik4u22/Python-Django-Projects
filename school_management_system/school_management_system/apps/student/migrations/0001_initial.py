# Generated by Django 4.1 on 2023-02-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('roll_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=150)),
                ('contact_no', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=100)),
                ('academic_year', models.CharField(max_length=20)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.TextField(default=True)),
                ('department_id', models.CharField(max_length=50)),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
    ]
