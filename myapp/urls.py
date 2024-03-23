from django.contrib.auth.views import LogoutView
from django.urls import path
from myapp import views
#from . import views
app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]