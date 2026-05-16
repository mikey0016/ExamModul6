import save
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from apps.models import User, Post


# Create your views here.

@login_required()
def dashboard_view(request):
    posts = Post.objects.all()
    post_count = 0
    for post in posts:
        post_count += post
    context = {'posts': posts, 'post_count': post_count}
    return render(request, 'dashboard.html', context)


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Bunday email royhatdan o'tilgan")
            return render(request, 'register.html')
        user = User(first_name=first_name,email=email)
        user.password = make_password(password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def login_view (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            user =queryset.first()
            if check_password(password , user.password):
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def create_post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content)
        return redirect('create_post')
    else:
        posts = Post.objects.filter(is_published=False)
        context = {'posts': posts}
        return render(request, 'create_post.html', context)

def post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.update(title=title, content=content)
        return redirect('dashboard')
    else:
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'post_detail.html', context)