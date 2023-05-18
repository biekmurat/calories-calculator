from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('recipe', views.home, name='recipe'),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),

]

