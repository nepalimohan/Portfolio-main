from django.contrib import admin
from .models import Profile, Education, Experience, FrontEndSkill, BackEndSkill, Project

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
    
@admin.register(FrontEndSkill)
class FrontEndSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'knowledge'] 
    
@admin.register(BackEndSkill)
class BackEndSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'knowledge']
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] 