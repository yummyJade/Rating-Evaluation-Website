from django.contrib import admin
# from .models import QuestionTitle, QuestionOption, QuestionFillingStatus

from .models import QuestionTitle, QuestionOption, QuestionResult, QuestionFillingStatus,QuestionResultOne, QuestionResultTwo
# Register your models here.

class QuestionTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'otype', 'qtype', )


class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titleId', 'content', 'value1', 'value2')


# class HolandTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'num', 'name')


class QuestionResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'qtype', 'value', 'type')


class QuestionFillingStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'qtype', 'finish', 'time')


class QuestionResultOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'qtype', 'des1', 'des2')


class QuestionResultTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'feature', 'contri', 'leaderP', 'studyP', 'trend', 'solveP', 'workE',
                    'weakness', 'suggest')

# admin.site.register(HollanderType, HolandTypeAdmin)

admin.site.register(QuestionTitle, QuestionTitleAdmin)
admin.site.register(QuestionOption, QuestionOptionAdmin)
admin.site.register(QuestionFillingStatus, QuestionFillingStatusAdmin)
admin.site.register(QuestionResult, QuestionResultAdmin)
admin.site.register(QuestionResultOne, QuestionResultOneAdmin)
admin.site.register(QuestionResultTwo, QuestionResultTwoAdmin)