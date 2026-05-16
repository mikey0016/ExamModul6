
from django.contrib import admin
from django.urls import path

from apps.views import dashboard_view, register_view, login_view, create_post_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('create_post/', create_post_view, name='create_post'),
]

