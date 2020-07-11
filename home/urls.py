from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('home/new', views.PostCreateView.as_view(), name='new_stocks'),
    path('home_info/<int:pk>/', views.Profile.as_view(), name='profile'), 
]
