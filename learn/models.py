from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name='类名', max_length=70)
    type = models.IntegerField(verbose_name='类型')


