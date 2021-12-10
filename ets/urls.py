from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:id>', views.single_landing, name='single_landing'),
    path('contactus/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
]