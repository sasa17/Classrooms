# Generated by Django 2.0.6 on 2018-07-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_student_exam_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('name', 'exam_grade')},
        ),
        migrations.AlterField(
            model_name='classroom',
            name='year',
            field=models.CharField(max_length=40),
        ),
    ]