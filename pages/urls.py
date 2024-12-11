from django.urls import path
from .views import HomePageView, AboutPageView, ProjectsView, ContactView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("contact/", ContactView.as_view(), name="contact"),
]
