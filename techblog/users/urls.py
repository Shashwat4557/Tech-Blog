from django.urls import path, include
from django.contrib.auth.views import LoginView
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
]