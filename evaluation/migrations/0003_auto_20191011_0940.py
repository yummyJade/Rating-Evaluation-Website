# Generated by Django 2.2.6 on 2019-10-11 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_remove_questionoption_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionoption',
            options={'verbose_name': '选项', 'verbose_name_plural': '选项'},
        ),
        migrations.AlterModelOptions(
            name='questiontitle',
            options={'verbose_name': '题目', 'verbose_name_plural': '题目'},
        ),
    ]
