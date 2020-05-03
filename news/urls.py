from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog-home'),
    path('news/new', views.CreateNewsView.as_view(), name='news-new'),
]

