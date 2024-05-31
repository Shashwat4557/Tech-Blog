from django.urls import path, include
from. import views

urlpatterns = [
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
]