from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type',)
    list_display_link = ('name',)


admin.site.register(Book, BookAdmin)  # 可见是一个注册事件

