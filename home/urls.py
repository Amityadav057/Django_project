from django.urls import path

from home.views import (
    home,
    school_create2,
    school_list,
    test_views,
    school_update,
    delete_school
)

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("home2", test_views, name="test"),
    path("school", school_list, name="school-list"),
    path("school-create", school_create2, name="school-create"),
    path("school-update/<int:id>/", school_update, name="school-update"),
    path("school-delete/<int:id>/", delete_school, name="school-delete"),
]