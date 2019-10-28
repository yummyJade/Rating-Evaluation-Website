# Generated by Django 2.2.6 on 2019-10-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_auto_20191017_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionFillingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=30, verbose_name='用户标识')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
                ('finish', models.CharField(default=0, max_length=1, verbose_name='完成情况')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=30, verbose_name='用户标识')),
                ('titleId', models.IntegerField(verbose_name='题目ID')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
                ('value', models.CharField(default=1, max_length=1, verbose_name='选项的值')),
                ('otype', models.CharField(max_length=20, verbose_name='题目类型')),
            ],
        ),
    ]