import email
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.

def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            print("user logged in")
            return redirect('profiles')
        else:
            messages.error(request, "Username OR Password is incorrect")
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was successfully logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    domain = "vedantu.com"
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            email_domain = user.email[user.email.index('@') + 1 : ].lower()
            if email_domain != domain:
                user.save()
                messages.success(request, 'User account was created!')
                login(request,user)
                return redirect('profiles')
            else:
                messages.error(request, 'Incorrect Email')
            

        else:
            messages.error(request, 'An error has occured during registration')


    context = {'page': page, 'form': form}
    return render(request, 'users/register.html', context)

def profiles(request):
    profiles = Profile.objects.filter(email__contains='@vedantu.com')
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description= '')

    context = {'profile' : profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):    
    profile = request.user.profile
    domain = "vedantu.com"
    email_domain = profile.email[profile.email.index('@') + 1 : ].lower()
    skills = profile.skill_set.all()
    projects = profile.post_set.all()

    context ={'profile': profile, 'domain': domain, 'email_domain': email_domain, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    form = ProfileForm()
    context ={'form': form}
    return render(request, 'users/profile_form.html', context)