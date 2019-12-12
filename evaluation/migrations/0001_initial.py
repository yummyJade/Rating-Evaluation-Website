# Generated by Django 2.2.6 on 2019-12-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionFillingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=30, verbose_name='用户标识')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
                ('finish', models.CharField(default=0, max_length=1, verbose_name='完成情况')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '作答情况',
                'verbose_name_plural': '作答情况',
            },
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleId', models.IntegerField(verbose_name='题目ID')),
                ('content', models.CharField(max_length=50, null=True, verbose_name='选项内容')),
                ('value1', models.CharField(default=1, max_length=1, verbose_name='选项1的值')),
                ('value2', models.CharField(default=1, max_length=1, verbose_name='选项2的值')),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
            },
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=30, verbose_name='用户标识')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
                ('value', models.IntegerField(default=1, verbose_name='选项的值')),
                ('type', models.IntegerField(default=0, verbose_name='类型')),
            ],
            options={
                'verbose_name': '结果',
                'verbose_name_plural': '结果',
            },
        ),
        migrations.CreateModel(
            name='QuestionResultOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
                ('type', models.IntegerField(default=0, verbose_name='类型')),
                ('des1', models.TextField(default='', verbose_name='结果描述1')),
                ('des2', models.TextField(default='', verbose_name='结果描述2')),
            ],
            options={
                'verbose_name': '结果返回',
                'verbose_name_plural': '结果返回',
            },
        ),
        migrations.CreateModel(
            name='QuestionResultTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4, verbose_name='类型')),
                ('feature', models.TextField(default='', verbose_name='特征')),
                ('contri', models.TextField(default='', verbose_name='对组织的贡献')),
                ('leaderP', models.TextField(default='', verbose_name='领导模式')),
                ('studyP', models.TextField(default='', verbose_name='学习模式')),
                ('trend', models.TextField(default='', verbose_name='倾向性顺序')),
                ('solveP', models.TextField(default='', verbose_name='解决问题模式')),
                ('workE', models.TextField(default='', verbose_name='工作环境倾向性')),
                ('weakness', models.TextField(default='', verbose_name='潜在缺点')),
                ('suggest', models.TextField(default='', verbose_name='潜在缺点发展建议')),
            ],
            options={
                'verbose_name': '结果返回',
                'verbose_name_plural': '结果返回',
            },
        ),
        migrations.CreateModel(
            name='QuestionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='问卷题目')),
                ('otype', models.CharField(max_length=20, verbose_name='题目类型')),
                ('qtype', models.CharField(max_length=20, verbose_name='问卷类型')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题目',
            },
        ),
    ]
