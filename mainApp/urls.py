from django.urls import path

from . import views

urlpatterns = [
    path(r'login', views.login, name='login'),
    path(r'', views.index, name='mainPage'),
    path('auth/logout', views.logout, name='index12'),
]