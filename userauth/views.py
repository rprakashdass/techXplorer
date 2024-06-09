from  django . shortcuts  import  get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserInfo, User_register, Hackathons, ExploreApi, AiModels
from django.contrib import messages

@login_required()
def home(request):
    return render(request, 'main.html')

def login_view(request):
  if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        userr = authenticate(request,username=username,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        invalid="Invalid Credentials"
        return render(request, 'login.html',{'invalid':invalid})

  return render(request, 'login.html')

def signup(request):
 try:
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        user_type = request.POST.get('user_type')

        my_user=User.objects.create_user(username, email, pwd)
        my_user.save()

        user_model = User_register.objects.create_user(password=pwd, email=email, username=username, user_type=user_type)
        user_model.save()

        if my_user is not None:
            login(request, my_user)
            return redirect('/')

 except:
        return redirect('home')
        invalid="User already exists"
        return render(request, 'signup.html',{'invalid':invalid})

 return render(request, 'signup.html')


@login_required()
def logout_user(request):
    logout(request)
    return redirect('/login_view', {'messages', 'succesfully logged out'})


@login_required()
def profile_update(request, username):
    user=User_register.objects.get(username=username)
    userr = UserInfo.objects.get_or_create(user=user)
    context = {
        'user_name' : username,
        'user_type' : user.user_type,
    }
    return render(request, 'profile.html', context)

@login_required()
def hackathons_feed(request):
    hackathons = Hackathons.objects.all()
    return render(request, 'hackathons_feed.html', {'hackathons': hackathons})


@login_required
def submit_hackathon_post(request, username):
    user = user=User_register.objects.get(username=username)
    location = 'India'
    if request.method == 'POST':
        # author = request.user
        caption = request.POST.get('caption')
        # posted_location = request.POST.get('posted_location')
        posted_support = request.POST.get('posted_support')
        queries = request.POST.get('queries')
        demo_link = request.POST.get('demo_link')
        post_image = request.FILES.get('post_image')
        post_video = request.FILES.get('post_video')

        hackathon_post = Hackathons(
            author=user,
            caption=caption,
            posted_location=location,
            posted_support=posted_support,
            queries=queries,
            demo_link=demo_link,
            post_image=post_image,
            post_video=post_video
        )
        hackathon_post.save()
        return redirect('home')

    return render(request, 'post.html', {'location' : location})
