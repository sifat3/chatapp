from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('chat/<int:pk>/', views.chat_view, name='chat')
]