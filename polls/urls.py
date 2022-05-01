from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('main', views.main, name = 'main'),
    path('home', views.index, name='WordMaster'),
    path('home/Word', views.Word, name='Word'),
    path('login', views.Login, name = "Login"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup_view, name="signup"),
]