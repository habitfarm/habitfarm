from django.urls import include, path

from . import views

app_name = 'webapp'
urlpatterns = [
    path("", view=views.home, name='home'),
    path(
        "habits/",
        include("webapp.habits.urls", namespace="habits"),
    ),
]
