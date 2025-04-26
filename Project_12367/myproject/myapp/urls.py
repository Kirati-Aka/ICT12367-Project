from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.create_poll, name='create_poll'),
    path('vote/<int:poll_id>/', views.vote_poll, name='vote_poll'),
    path('result/<int:poll_id>/', views.poll_result, name='poll_result'),
    path('poll/<int:poll_id>/edit/', views.edit_poll_options, name='edit_poll_options'),
]
