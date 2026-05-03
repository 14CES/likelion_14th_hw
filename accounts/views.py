from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from .models import Profile

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:postpage')
        else:
            return render(request,'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:postpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {'error' : '이미 존재하는 아이디입니다.'})
        
        if request.POST['password'] == request.POST['confirm']:
            newuser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            nickname=request.POST['nickname']
            major=request.POST['major']
            profile_image=request.FILES.get('profile_image')
            phonenumber=request.POST['phonenumber']

            profile = Profile(
                user=newuser,
                nickname=nickname,
                major=major,
                profile_image=profile_image,
                phonenumber=phonenumber,
            )
            profile.save()

            auth.login(request, newuser)
            return redirect('main:postpage')
        
    return render(request, 'accounts/signup.html')
