# Generated by Django 2.2.6 on 2019-10-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0013_questionfillingstatus_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiontitle',
            name='name',
            field=models.CharField(max_length=100, verbose_name='问卷题目'),
        ),
    ]
