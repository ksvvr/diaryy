from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homelogin'),
    path('signup', views.signup, name='signup'),
    path('signupUser', views.signupUser, name='signupUser'),
    path('login', views.loginUser, name='signinUser'),
    path('index', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('read/', views.view_entries, name='read'),
    path('write/', views.write, name='write'),
    path('about/', views.about, name='about'),
    path('entry/', views.create_entry, name='entry'),
]

