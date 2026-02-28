from django.urls import path

from user.views import register, user_login, logout_user
urlpatterns = [
    path('register',register, name="register" ),
    path('login/',user_login, name="login" ),
    path('logout/',logout_user, name="logout" ),


]