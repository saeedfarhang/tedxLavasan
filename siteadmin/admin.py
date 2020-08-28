from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass