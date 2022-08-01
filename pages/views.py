from django.shortcuts import render
from .models import Education, Experience, Profile

# Create your views here.
def home(request):
    if request.method == "POST":
        pass
    profile =  Profile.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    data = {
        'profile': profile,
        'education': education,
        'experience': experience,
    }
    return render(request, 'pages/home.html', data)