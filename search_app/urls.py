from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='search_url'),
    path('thank-you', views.ThankYouView.as_view()),
    path('error.html', views.ErrorView.as_view()),
]
