from django.urls import path
from . import views

# url_base = http://127.0.0.1:8000/

urlpatterns = [
    path('login', views.login_view, name = 'login'),
    path('register', views.register_view, name = 'register'),
    path('logout', views.logout_view, name = "logout")
]
