from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'teacher', 'credits']

class TaskAdmin(admin.ModelAdmin):

    # columnas a mostrarse en el panel administrador para el momento de registro de tareas
    fields = ['title', 'description', 'course']

    list_display = ['title', 'description', 'course', 'completed']

    def mark_as_completed(modeladmin, request, queryset):
        queryset.update(completed = True)

    def mark_as_not_completed(modeladmin, request, queryset):
        queryset.update(completed = False)

    def assing_specific_course(modeladmin, request, queryset):
        specific_id = 1
        course = models.Course.objects.get(id = specific_id)
        queryset.update(course = course)

    mark_as_completed.short_description = "Marcar tareas como completadas"
    mark_as_not_completed.short_description  = "Marcar tareas como NO completadas"
    assing_specific_course.short_description  = "Asignar taraes a curso por defect"

    actions = [
        mark_as_completed,
        mark_as_not_completed,
        assing_specific_course
    ]

admin.site.register(models.Task, TaskAdmin)