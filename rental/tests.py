# rental/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Drone, Rental
from .forms import RentalForm
from datetime import datetime, timedelta
from django.utils import timezone

class DroneListViewTests(TestCase):
    def setUp(self): #Test için datalar hazırlanır
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.drone = Drone.objects.create(
            brand='TestBrand',
            model='TestModel',
            category='TestCategory',
            weight=2.5,
            price_per_hour=50.0,
            availability=True
        )

    def test_drone_list_view(self): #Drone list status code 200'e eşitlenerek true sonuç vermesi beklenir
        response = self.client.get(reverse('drones_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_rental_booking_view(self):
        response = self.client.get(reverse('rental_booking', args=[self.drone.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_rental_view(self): #Kiralama işleminin silinmesinin ardından status code, JSON message, kiralama id bulunma durumu ve drone uygunluğu kontrol edilir
        rental = Rental.objects.create(user=self.user, drone=self.drone, start_time=timezone.now(), end_time=timezone.now() + timedelta(days=1))
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_rental', args=[rental.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Rental deleted successfully'})
        self.assertFalse(Rental.objects.filter(id=rental.id).exists())
        self.drone.refresh_from_db()
        self.assertTrue(self.drone.availability)
    
    def test_update_rental_view(self): #Silme işlemindekilere ek olarak başlangıç ve bitiş tarihleri eşitlenerek ekstra kontrol edilir.
        rental = Rental.objects.create(user=self.user, drone=self.drone, start_time=timezone.now(), end_time=timezone.now() + timedelta(days=1))
        self.client.login(username='testuser', password='testpassword')
        new_start_time = timezone.now() + timedelta(days=2)
        new_end_time = timezone.now() + timedelta(days=3)
        response = self.client.post(reverse('update_rental', args=[rental.id]), {
            'start_time': new_start_time,
            'end_time': new_end_time,
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Rental updated successfully'})
        rental.refresh_from_db()
        self.assertEqual(rental.start_time, new_start_time)
        self.assertEqual(rental.end_time, new_end_time)
        self.drone.refresh_from_db()
        self.assertFalse(self.drone.availability)