from django.shortcuts import render,get_object_or_404
from .models import *


def cv_page(request):
    
    profile = get_object_or_404(Profile,default = True)
    skills = Skill.objects.filter(profile = profile)
    link = Link.objects.filter(profile = profile).first()
    desc = ProfileDescription.objects.filter(profile = profile).first()
    projects = Project.objects.filter(profile=profile)
    education = Education.objects.filter(profile = profile)
    
    context = {
        'profile':profile,
        'skills':skills,
        'link':link,
        'desc':desc,
        'projects':projects,
        'education':education,
        }
    return render(request,"index.html",context)


def profile_page(request,name):
    profile = get_object_or_404(Profile,name = name)
    
    skills = Skill.objects.filter(profile = profile)
    link = Link.objects.filter(profile = profile).first()
    desc = ProfileDescription.objects.filter(profile = profile).first()
    projects = Project.objects.filter(profile = profile)
    education = Education.objects.filter(profile = profile)
    
    context = {
        'profile':profile,
        'skills':skills,
        'link':link,
        'desc':desc,
        'projects':projects,
        'education':education,
        }
    
    return render(request,"index.html",context)