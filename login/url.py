from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('login', views.login, name='login'),
    path('login/account', views.login, name='login'),
]