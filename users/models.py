from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=50)
    password = models.CharField(verbose_name='密码', max_length=50)
