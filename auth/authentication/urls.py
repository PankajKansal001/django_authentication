from django.contrib import admin
from django.urls import path
from authentication import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signp',views.signup,name="signp"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uid64>/<token>',views.activate,name="activate"),
]