from django.urls import path
from . import views

urlpatterns = [
    path('', views.getApi, name='getApi'),
    path('videos/', views.VideoListView.as_view(), name='Videos'),
]