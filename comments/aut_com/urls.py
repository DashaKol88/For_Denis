from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_author, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    ]