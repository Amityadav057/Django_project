
from django.urls import path
from home.views import home, test_views, school_list

urlpatterns = [
    path('',home, name="home"),
    path('home2', test_views, name="test"),
    path('school', school_list, name = "school-list")
]