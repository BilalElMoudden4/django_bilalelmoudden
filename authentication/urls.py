from django.urls import path
from .views import login_view, home_view, login_session_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login-session/', login_session_view, name='login_session'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]
