from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path('Register', views.register, name='register'),
    path("Recommend", views.iris_predict, name="iris_predict"),
    path("Courses", views.Courses, name="courses"),


]

 