from django.urls import path

from .views import *

urlpatterns = [
    path("", homepage, name=""),
    path("color/", colorname, name="color12"),
    path("city/", citypage, name="city"),
    path("phone/", phonepage, name="phone"),
    path("movie/", moviepage, name="movie"),
    path("indexform/", indexformpage, name="indexform")
]