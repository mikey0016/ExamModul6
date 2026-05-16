import save
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from apps.models import User, Post


# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    if request.method == 'POST':
        pass
    else:

        return render(request, 'dashboard.html')


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

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            user = queryset.first()
            if user.check_password(password):
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request,"Bunday email mavjud emas!")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def create_post_view(request):
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
        return redirect('create_post')
    else:
        posts = Post.objects.filter(is_published=False)
        context = {'posts': posts}
        return render(request, 'create_post.html', context)
