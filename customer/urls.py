from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('', views.home,name='home'),
     path('register/', views.register,name='register'),
     path('login/', views.login,name='login'),
     path('login/loggedin/', views.loggedin,name='loggedin'),
      path('logout/', views.logout,name='logout'),
      path('login/logout/', views.logout,name='logout'),
      path('loggedin/logout/', views.logout,name='logout'),
       path('loggedin/', views.loggedin,name='loggedin'),

]