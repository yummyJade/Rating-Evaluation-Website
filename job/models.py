from django.db import models

# Create your models here.


# 关于职业类型的几种分类及对照
class NumAndType(models.Model):
    num = models.IntegerField(verbose_name='编号')
    name = models.CharField(verbose_name='类名', max_length=20)
    type = models.CharField(verbose_name='类型', max_length=20, default='')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name

# 关于职业价值观测试的几种分类
# 利他主义	美感	智力	成就感	自主	社会地位	管理	经济报酬	社会交际	安全稳定	舒适	团队	新奇
# class JobValuesType(models.Model):
#     name = models.IntegerField(verbose_name='编号')
#     name = models.CharField(verbose_name='类名', max_length=10)


# 职业的对应表
class JobScore(models.Model):
    name = models.CharField(verbose_name='职业名称', max_length=50)
    htype1 = models.IntegerField(verbose_name='常规型')
    htype2 = models.IntegerField(verbose_name='现实型')
    htype3 = models.IntegerField(verbose_name='研究型')
    htype4 = models.IntegerField(verbose_name='管理型')
    htype5 = models.IntegerField(verbose_name='社会型')
    htype6 = models.IntegerField(verbose_name='艺术型')

    valtype1 = models.IntegerField(verbose_name='利他主义', default=0)
    valtype2 = models.IntegerField(verbose_name='美感', default=0)
    valtype3 = models.IntegerField(verbose_name='智力挑战', default=0)
    valtype4 = models.IntegerField(verbose_name='成就感', default=0)
    valtype5 = models.IntegerField(verbose_name='自主', default=0)
    valtype6 = models.IntegerField(verbose_name='社会地位', default=0)
    valtype7 = models.IntegerField(verbose_name='管理', default=0)
    valtype8 = models.IntegerField(verbose_name='经济报酬', default=0)
    valtype9 = models.IntegerField(verbose_name='社会交际', default=0)
    valtype10 = models.IntegerField(verbose_name='安全感', default=0)
    valtype11 = models.IntegerField(verbose_name='舒适', default=0)
    valtype12 = models.IntegerField(verbose_name='团队', default=0)
    valtype13 = models.IntegerField(verbose_name='新奇', default=0)

    class Meta:
        verbose_name = '职业打分'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


# 职业的对照表 第二个打分项
class Jobscore2(models.Model):
    name = models.CharField(verbose_name='职业名称', max_length=50)
    valtype1 = models.IntegerField(verbose_name='利他主义', default=0)
    valtype2 = models.IntegerField(verbose_name='美感', default=0)
    valtype3 = models.IntegerField(verbose_name='智力挑战', default=0)
    valtype4 = models.IntegerField(verbose_name='成就感', default=0)
    valtype5 = models.IntegerField(verbose_name='自主', default=0)
    valtype6 = models.IntegerField(verbose_name='社会地位', default=0)
    valtype7 = models.IntegerField(verbose_name='管理', default=0)
    valtype8 = models.IntegerField(verbose_name='经济报酬', default=0)
    valtype9 = models.IntegerField(verbose_name='社会交际', default=0)
    valtype10 = models.IntegerField(verbose_name='安全感', default=0)
    valtype11 = models.IntegerField(verbose_name='舒适', default=0)
    valtype12 = models.IntegerField(verbose_name='团队', default=0)
    valtype13 = models.IntegerField(verbose_name='新奇', default=0)

    class Meta:
        verbose_name = '职业价值观打分'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


