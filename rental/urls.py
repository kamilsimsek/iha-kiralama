from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#Gerekli url tanımları yapılır
urlpatterns = [
    path('', include('users.urls')),
    path('drones_list/', views.drone_list, name='drones_list'),
    path('rental/<int:drone_id>/', views.rental_booking, name='rental_booking'),
    path('rental/<int:rental_id>/delete', views.delete_rental, name='delete_rental'),
    path('rental/<int:rental_id>/update', views.update_rental, name='update_rental'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]