# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # The login view is the homepage.
    path('', views.login_view, name='home'),

    # The welcome, logout, chat, and test pages have their own paths.
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', views.chat_page, name='chat_page'),
    path('test/', views.test_page, name='test_page'),
]