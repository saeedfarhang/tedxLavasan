from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.IntroSpeaker)
class IntroSpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass