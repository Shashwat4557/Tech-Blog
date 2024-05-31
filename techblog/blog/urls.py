from django.urls import path, include
from. import views
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView

urlpatterns = [
    path('search/', views.search, name='search'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('blog_list/', views.blog_list, name='blog_list'),
]