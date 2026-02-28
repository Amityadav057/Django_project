from django.urls import path


from .class_based_views import StudentListView
urlpatterns = [
    path('', StudentListView.as_view(), name = "student-class")
]