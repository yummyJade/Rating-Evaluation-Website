# Generated by Django 2.2.6 on 2019-10-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_auto_20191017_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionoption',
            name='content',
            field=models.CharField(default='', max_length=50, verbose_name='选项内容'),
        ),
    ]
