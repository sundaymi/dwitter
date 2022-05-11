from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import DweetForm, SignUpForm, LoginForm

# Create your views here.

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
        
    followed_dweets = Dweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
    # form = DweetForm()
    return render(request, "dwitter/dashboard.html", {"form": form , "dweets": followed_dweets}) 
    


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'dwitter/profile_list.html', {'profiles': profiles})


def profile(request,pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
    # pk stands for primary key id, its required for a call to our db  


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            return "Welcome to Dwitter!"
        
    else:
        form = SignUpForm() 
    return render(request, 'dwitter/signup.html', {'form': form})


def login(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         pass 
    # else:
    #     form = LoginForm()
    return render(request, 'dwitter/login.html', )  #{'form': form}


        
