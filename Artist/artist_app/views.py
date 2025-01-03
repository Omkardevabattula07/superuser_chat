from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Userprofile
from django.contrib import messages
# Create your views here.
def base_art(request):
    return render (request,"base_artist.html")
def register_art(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check'] 
        bio = request.POST.get('bio',"")
        profile_pic = request.FILES.get("profile_pic",None)
        security_answer = request.POST['security_answer'] 
        if password != password_check:
            return redirect('register_art') 
        if User.objects.filter(username=username).exists():
            return redirect("register_art") 
        user = User.objects.create(username=username,password=password, )   
        user_profile = Userprofile.objects.create(user=user,bio= bio,profile_pic = profile_pic,security_answer=security_answer) 
        user.save()
        user_profile.save()
        
        return redirect("login_art")

    
    return render(request,'register_artist.html',{'messages':messages})
def login_art(request):
    return render(request,'login_artist.html')