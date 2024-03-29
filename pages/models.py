from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

work_choices = (
    ('Freelancer', 'Freelancer'),
    ('UI/UX Designer', 'UI/UX Designer'),
    ('Django Developer', 'Django Developer'),
)

freelance_choices = (
    ('Availabe', 'Availabe'),
    ('Unavailabe', 'Unavailabe'),
)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    works_as = MultiSelectField(choices=work_choices, max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    freelance = models.CharField(choices=freelance_choices, max_length=50)
    degree = models.CharField(max_length=100)
    about = models.TextField()
    facebook_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    image = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    course_name = models.CharField(max_length=100)
    duration_from = models.PositiveIntegerField(blank=True, null=True)
    duration_to = models.PositiveIntegerField(blank=True, null=True)
    name_of_institute = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.course_name
    
class Experience(models.Model):
    post = models.CharField(max_length=100)
    name_of_organization = models.CharField(max_length=100)
    time_period = models.PositiveIntegerField()
    address = models.CharField(max_length=100, blank=True)
    responsibilities = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.post
    
class FrontEndSkill(models.Model):
    name = models.CharField(max_length=50)
    knowledge = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class BackEndSkill(models.Model):
    name = models.CharField(max_length=50)
    knowledge = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='photots/thumbnails/')
    description = models.TextField()
    link = models.URLField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
    