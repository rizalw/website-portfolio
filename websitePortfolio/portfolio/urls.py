from django.urls import path
from django.urls import path
from . import views


# Buat mengatur url, kalo di flask itu @app.route()
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("certifications", views.certifications, name="certifications")
]