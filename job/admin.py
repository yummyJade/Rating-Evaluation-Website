from django.contrib import admin
from .models import NumAndType, JobScore, Jobscore2


# Register your models here.
class NumAndTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'num', 'name', 'type')


class JobScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'htype1', 'htype2', 'htype3', 'htype4', 'htype5', 'htype6',  'valtype1', 'valtype2', 'valtype3', 'valtype4', 'valtype5', 'valtype6', 'valtype7',
                    'valtype8', 'valtype9', 'valtype10', 'valtype11', 'valtype12', 'valtype13')


class JobScore2Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'valtype1', 'valtype2', 'valtype3', 'valtype4', 'valtype5', 'valtype6', 'valtype7',
                    'valtype8', 'valtype9', 'valtype10', 'valtype11', 'valtype12', 'valtype13')


admin.site.register(NumAndType, NumAndTypeAdmin)
admin.site.register(JobScore, JobScoreAdmin)
admin.site.register(Jobscore2, JobScore2Admin)
