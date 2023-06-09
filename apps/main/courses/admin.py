# Django
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.courses.models import CourseCategory, Course


class CourseInline(admin.TabularInline):
    model = Course


@admin.register(CourseCategory)
class CourseCategoryAdmin(TranslationAdmin):
    inlines = [
        CourseInline
    ]
    list_display = ['name', 'created_date', 'last_updated']
    list_display_links = ('name',)
    list_filter = ['name']


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ['name', 'category', 'price', 'course_duration']
    list_display_links = ('name', 'category')
    list_filter = ['category', 'price']
