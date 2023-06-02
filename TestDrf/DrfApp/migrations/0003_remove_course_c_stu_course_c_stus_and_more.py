# Generated by Django 4.0.4 on 2023-05-31 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DrfApp', '0002_alter_student_s_cla_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='c_stu',
        ),
        migrations.AddField(
            model_name='course',
            name='c_stus',
            field=models.ManyToManyField(related_name='s_courses', to='DrfApp.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_cla_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cla_stus', to='DrfApp.class'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_tea', to='DrfApp.course'),
        ),
    ]