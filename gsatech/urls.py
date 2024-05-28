from django.urls import path
from gsatech import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registration/', views.RegistrationformView.as_view(), name='register'),
    path('taskform/', views.taskform, name='taskform')
]