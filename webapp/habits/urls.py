from django.urls import path

from . import views

app_name = 'habits'
urlpatterns = [
    path("", view=views.habit_list, name='list'),
    path("create", view=views.habit_create, name='create'),
]
