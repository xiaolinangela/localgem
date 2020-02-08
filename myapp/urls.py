from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new_search/', views.new_search, name='new_search'),
    path('used_cars/', views.used_cars, name='used_cars'),
    path('electronics/', views.electronics, name='electronics'),
    path('fashion/', views.fashion, name='fashion'),
    path('jobs/', views.jobs, name='jobs'),
    path('toys/', views.toys, name='toys'),
    path('housing/', views.housing, name='housing'),
]