from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rental import views

router = routers.DefaultRouter()
router.register(r'drones', views.DroneViewSet)
router.register(r'rentals', views.RentalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', views.home, name='home'),  # Ana sayfa
    path('drones/', views.drone_list, name='drone_list'),  # Drone listesi
    path('', include('rental.urls')),
    path('', include('users.urls')),
]
