from django.urls import path

from .views import RecommendView


app_name = "recommendation"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('recommend/', RecommendView.as_view()),
]