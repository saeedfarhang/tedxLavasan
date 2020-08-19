from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Signup)
class SignupAdmin(admin.ModelAdmin):
    pass

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.HowYouKnowUs)
class HowYouKnowUsAdmin(admin.ModelAdmin):
    pass