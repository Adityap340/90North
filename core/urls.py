from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core\login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
