from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form_view),
    path('', views.home, name = "home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name = "menu"),
    path('booking/', views.reservation, name = "booking"),

]