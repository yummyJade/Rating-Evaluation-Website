from django.db import models

# Create your models here.

# 问卷类
# 问卷类型，现有类型为
# 1.Hollander---A
# 2.MBTI ---B
# 3.
#
# class QTypes(models.Model):
#     name = models.CharField(verbose_name='问卷类型', max_length=20)
#
# # 题目类型，现有类型为
#
#
# class OTypes(models.Model):
#     name = models.CharField(verbose_name='题目类型', max_length=20)


# 问卷题目
class QuestionTitle(models.Model):
    name = models.CharField(verbose_name='问卷题目', max_length=100)
    otype = models.CharField(verbose_name='题目类型', max_length=20)
    qtype = models.CharField(verbose_name='问卷类型', max_length=20)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


# 问卷选项
class QuestionOption(models.Model):
    titleId = models.IntegerField(verbose_name='题目ID')
    content = models.CharField(verbose_name='选项内容', max_length=50, null=True)
    value1 = models.CharField(verbose_name='选项1的值', max_length=1, default=1)
    value2 = models.CharField(verbose_name='选项2的值', max_length=1, default=1)

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.verbose_name



# 第二种问卷的选项，只有是 否

# # 关于霍兰德职业类型的几种分类
# class HollanderType(models.Model):
#     num = models.IntegerField(verbose_name='编号')
#     name = models.CharField(verbose_name='类名', max_length=10)
#     class Meta:
#         verbose_name = '分类'
#         verbose_name_plural = verbose_name
#
#         def __str__(self):
#             return self.name


# 问卷结果
class QuestionResult(models.Model):
    userId = models.CharField(verbose_name='用户标识', max_length=30)
    qtype = models.CharField(verbose_name='问卷类型', max_length=20)
    value = models.IntegerField(verbose_name='选项的值', default=1)
    type = models.IntegerField(verbose_name='类型')

    class Meta:
        verbose_name = '结果'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


# 问卷结果返回的值
class QuestionResultOne(models.Model):
    qtype = models.CharField(verbose_name='问卷类型', max_length=20)
    type = models.IntegerField(verbose_name='类型')
    des1 = models.TextField(verbose_name='结果描述1',default="")
    des2 = models.TextField(verbose_name='结果描述2', default="")


    class Meta:
        verbose_name = '结果返回'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name

# 问卷结果返回的值
# 类型	特征	  对组织的贡献	领导模式	  学习模式	倾向性顺序	解决问题模式	工作环境倾向性	潜在缺点	发展建议

class QuestionResultTwo(models.Model):
    # qtype = models.CharField(verbose_name='问卷类型', max_length=20)
    type = models.CharField(verbose_name='类型', max_length=4)
    feature = models.TextField(verbose_name='特征', default="")
    contri = models.TextField(verbose_name='对组织的贡献', default="")
    leaderP = models.TextField(verbose_name='领导模式', default="")
    studyP = models.TextField(verbose_name='学习模式', default="")
    trend = models.TextField(verbose_name='倾向性顺序', default="")
    solveP = models.TextField(verbose_name='解决问题模式', default="")
    workE = models.TextField(verbose_name='工作环境倾向性', default="")
    weakness =  models.TextField(verbose_name='潜在缺点', default="")
    suggest = models.TextField(verbose_name='潜在缺点发展建议', default="")

    class Meta:
        verbose_name = '结果返回'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


# 问卷回答情况
# todo：其实甚至可以加上时间标记
class QuestionFillingStatus(models.Model):
    userId = models.CharField(verbose_name='用户标识', max_length=30)
    qtype = models.CharField(verbose_name='问卷类型', max_length=20)
    finish = models.CharField(verbose_name='完成情况', max_length=1, default=0)  # 即完成或未完成
    time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = '作答情况'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.name
