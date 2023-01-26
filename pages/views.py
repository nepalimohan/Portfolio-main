from django.shortcuts import render, redirect
from .models import (Education, Experience, Profile, FrontEndSkill, 
                     BackEndSkill, Project)
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    profile =  Profile.objects.all().last()
    education = Education.objects.all()
    experience = Experience.objects.all()
    front_skills = FrontEndSkill.objects.all()
    back_skills = BackEndSkill.objects.all()
    project = Project.objects.all().order_by('id')
    
    data = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'front_skills': front_skills,
        'back_skills' : back_skills,
        'project' : project,
    }
    return render(request, 'pages/home.html', data)

def contact(request):
    if request.method == "POST":
        name =  request.POST['name']
        email =  request.POST['email']
        subject =  request.POST['subject']
        message =  request.POST['message']

    # admin_info = 'User.objects.get(is_superuser= True)'
    admin_email = 'nepalimohan@outlook.com'

    send_mail(
        'You have received message from ' + name + ' whose email is ' + email + ' regarding ' + subject,
        message,
        'nepali.mohan11@gmail.com',
        [admin_email],
        fail_silently=False,
    )
    
    return redirect('home')