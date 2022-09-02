from django.shortcuts import render
from .models import Education, Experience, Profile, FrontEndSkill, BackEndSkill

# Create your views here.
def home(request):
    if request.method == "POST":
        pass
    profile =  Profile.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    front_skills = FrontEndSkill.objects.all()
    back_skills = BackEndSkill.objects.all()
    
    
    data = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'front_skills': front_skills,
        'back_skills' : back_skills,
    }
    return render(request, 'pages/home.html', data)