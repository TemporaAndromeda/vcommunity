


from django.shortcuts import render, redirect
from django.db.models import Q
from users.models import Profile, Skill


def searchProfiles(request):
    search_query = ''

    if request.GET.get('text'):
        search_query =  request.GET.get('text')
    

    skills = Skill.objects.filter(name__icontains= search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |  
         Q(skill__in=skills))

    return profiles, search_query