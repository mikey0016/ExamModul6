import save
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from apps.models import User, Post


# Create your views here.

def dashboard_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        views = request.POST.get('views')
        author_id = request.POST.get('author_id')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')
        Post.objects.create(title=title, content=content, is_published=is_published, views=views,author_id=author_id, created_at=created_at,
                     updated_at=updated_at)
        save()
        return redirect('dashboard')
    else:
        posts = Post.objects.filter(is_published=False)
        context = {'posts': posts}
        return render(request, 'dashboard.html', context)


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Bunday email royhatdan o'tilgan")
            return render(request, 'register.html')
        user = User(first_name=first_name,username=username,password=make_password(password))
        user.password = make_password(password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            user = queryset.first()
            if user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        return render(request, 'login.html')

def create_post_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'create_post.html')

def post_detail_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'post_detail.html')