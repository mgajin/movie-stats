from django.contrib import admin
from django.urls import path
from .views import HomeView, NotFoundView

urlpatterns = [
    path('', HomeView.as_view()),
    path('error/not-found', NotFoundView.as_view())
]
