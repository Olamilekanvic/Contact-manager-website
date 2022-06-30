from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('casual/', views.casual, name='casual'),
    path('family/', views.family, name='family'),
    path('private/', views.private, name='private'),
    path('work/', views.work, name='work'),
    path('contacts/<int:pk>/', views.edit, name='edit'),
    path('contacts/<int:pk>/delete', views.delete, name='delete'),
    
]
