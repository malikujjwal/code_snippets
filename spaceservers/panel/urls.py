from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="server-settings"),
    path('mods/', views.mods, name="server-mods")
]