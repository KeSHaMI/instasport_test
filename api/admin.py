from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Workout, WorkoutAdmin)