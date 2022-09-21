from django.contrib import admin
from .models import Task, TodaysTask, DaysOfTheWeek, AdhockTask

# Register your models here.
admin.site.register(DaysOfTheWeek)

admin.site.register(Task)

admin.site.register(TodaysTask)

admin.site.register(AdhockTask)