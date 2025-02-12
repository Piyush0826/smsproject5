# Generated by Django 5.0.7 on 2024-10-07 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
        ('facultyapp', '0002_rename_blogpost_facultypost'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced Object-Oreinted Programming'), ('PFSD', 'Python Full Stack Development'), ('DBMS', 'Database Management System'), ('NPS', 'Network Protocol and Security')], max_length=50)),
                ('section', models.CharField(choices=[('S11', 'Section 11'), ('S12', 'Section 12'), ('S13', 'Section 13'), ('S14', 'Section 14'), ('S15', 'Section 15')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]
