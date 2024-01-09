from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_author, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    ]