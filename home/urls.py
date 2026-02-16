from django.urls import path
from home.views import home, test_views 


urlpatterns = [
    path('', home, name="home"),
    path('home2', test_views, name="test")
]
