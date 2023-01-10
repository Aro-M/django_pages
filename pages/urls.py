from django.urls import path
from .views import HomePageView, AboutPageView, CareerPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("career/", CareerPageView.as_view(), name="career"),
    path("", HomePageView.as_view(), name="home"),
]
