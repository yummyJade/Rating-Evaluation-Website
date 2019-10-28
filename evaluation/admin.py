from django.contrib import admin
from .models import QuestionTitle, QuestionOption, QuestionResult, QuestionFillingStatus


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

# admin.site.register(HollanderType, HolandTypeAdmin)
admin.site.register(QuestionTitle, QuestionTitleAdmin)
admin.site.register(QuestionOption, QuestionOptionAdmin)
admin.site.register(QuestionFillingStatus, QuestionFillingStatusAdmin)
admin.site.register(QuestionResult, QuestionResultAdmin)
