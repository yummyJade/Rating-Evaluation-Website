# Generated by Django 2.2.6 on 2019-10-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20191024_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumAndType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='编号')),
                ('name', models.CharField(max_length=20, verbose_name='类名')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.DeleteModel(
            name='HollanderType',
        ),
    ]