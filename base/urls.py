from django.urls import path
from . import views

urlpatterns = [
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name= "profile"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path('delete-message/<str:pk>/', views.deleteMessages, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activities/', views.activityPage, name="activities"),
]