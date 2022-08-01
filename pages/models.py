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
    duration_from = models.DateField()
    duration_to = models.DateField()
    name_of_institute = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.course_name
    
class Experience(models.Model):
    post = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    responsibilities = models.TextField()
    
    def __str__(self):
        return self.post
    