# Generated by Django 4.2.6 on 2023-10-09 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degreechecklist', '0002_remove_transfer_credit_course_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreRequisite_Course',
        ),
        migrations.RemoveField(
            model_name='degree',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='degree',
            name='course_name',
        ),
        migrations.AddField(
            model_name='course',
            name='prereq_course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='prereq_course_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
