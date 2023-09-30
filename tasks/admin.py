from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TaskType, Position, Worker, Team, Project, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("workers",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("workers",)


admin.site.register(TaskType, Project, Team)
