from django.contrib import admin
from .models import Profile, Education, Experience

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'phone', 'email', 'address']
    list_display_links = ['id', 'name']
    

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_of_institute']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'address']