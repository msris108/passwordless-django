from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index, name=""),
    path("get-current-user/", views.getCurrentUser, name="getCurrentUser"),
    path("get-user-by-email/<str:email>", views.getUserByEmail, name="getUserByEmail"),
]