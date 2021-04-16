from django.urls import path
from .import views

app_name = "assignments"

urlpatterns=[
    path("",views.index,name="index"),
    path("delete/",views.delete_task,name="delete"),
    path("task/completed/",views.completed,name="completed"),
    path("register/",views.register,name="register"),
    path("home/",views.home,name="home"),
    path("assignment/<int:ass_id>",views.assignment,name="assignment"),
    path("solutions/<int:ass_id>",views.solutions,name="solution"),
    path("solution/<int:ass_id>",views.Solution_specific,name="single_solution"),
    path("solution/submit/<int:ass_id>",views.submit,name="submit"),
    path("user/logged/in",views.login_manually,name="logged_in"),


    path("logout/",views.logout,name="logout_redirect")
]