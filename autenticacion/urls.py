from django.urls import path
from . import views

urlpatterns = [
    # Login con sesión
    path("login/", views.login_session_view, name="login"),
    path("home/", views.home_view, name="home"),
    
    # Login sin sesión
    path("login_no_session/", views.login_view, name="login_no_session"),
    path("home_no_session/", views.home_no_session_view, name="home_no_session"),
    
    # Logout (se usará para la funcionalidad con sesión; también se asegura de limpiar cualquier dato temporal)
    path("logout/", views.logout_view, name="logout"),
]
