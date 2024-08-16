

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.Register_user, name="register" ),
    path('login/', views.user_login, name='user_login'),
    path('logout_user/', views.logout_user, name='logout_user')
]
