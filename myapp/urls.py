from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    # path('new-search/', views.new_search, name='new_search'),
]