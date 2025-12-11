from django.contrib import admin
from .models import (
    Teacher, Subject, Course, Module, Content,
    Text, Video, Image, File
)

# ----------------- Teacher -----------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'expertise', 'experience_years', 'is_active', 'created_at')
    list_filter = ('is_active', 'expertise')
    search_fields = ('full_name', 'expertise')
    ordering = ('full_name',)


# ----------------- Subject -----------------
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


# ----------------- Course -----------------
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'subject', 'created_at')
    list_filter = ('subject',)
    search_fields = ('title', 'owner__full_name')
    inlines = [ModuleInline]
    prepopulated_fields = {'slug': ('title',)}


# ----------------- Module -----------------
class ContentInline(admin.TabularInline):
    model = Content
    extra = 0


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [ContentInline]
    search_fields = ('title', 'course__title')


# ----------------- Content -----------------
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('module', 'content_type', 'object_id')
    list_filter = ('content_type',)
    search_fields = ('module__title',)


# ----------------- Items -----------------
@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'owner__full_name')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'url', 'created_at')
    search_fields = ('title', 'owner__full_name')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'image', 'created_at')
    search_fields = ('title', 'owner__full_name')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'file', 'created_at')
    search_fields = ('title', 'owner__full_name')
