from django.urls import path
from . import views

app_name = 'movies'
# All URLS start with /movies + path in this mini-app
urlpatterns = [
  path("",views.index,name="index"),
  path("<int:movie_id>", views.details, name="details")
]
                                  