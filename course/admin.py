from django.contrib import admin
from .models import Course, CourseLog


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'updated_at')
    search_fields = ('title', 'instructor')
    list_filter = ('updated_at',)


@admin.register(CourseLog)
class CourseLogAdmin(admin.ModelAdmin):
    list_display = ('course', 'action', 'timestamp')
    search_fields = ('course__title', 'action')
    list_filter = ('action', 'timestamp')

