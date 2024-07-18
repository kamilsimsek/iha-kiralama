from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Drone, Rental
from .serializer import DroneSerializer, RentalSerializer
from .forms import RentalForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAdminUser]  # Sadece admin kullanıcılar erişebilir

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAdminUser] 

@login_required
def drone_list(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest': #Get isteği ve Ajax kontrolü sağlanır
        brand = request.GET.get('brand', '')
        weight = request.GET.get('weight', '')

        drones = Drone.objects.filter(availability=True) #Drone müsaitliği olanlar listelenir
        
        if brand:
            drones = drones.filter(brand=brand) #Markaya göre filtreleme sağlanır

        if weight:
            weight_ranges = {
                '0-10': (0, 10),
                '10-20': (10, 20),
                '20-30': (20, 30),
                '30-40': (30, 40),
                '40+': (40, float('inf')),
            }
            if weight in weight_ranges:
                min_weight, max_weight = weight_ranges[weight]
                drones = drones.filter(weight__gte=min_weight, weight__lt=max_weight) #Ağırlığa göre filtreleme sağlanır

        data = []
        for drone in drones:
            data.append({
                "brand": drone.brand,
                "model": drone.model,
                "category": drone.category,
                "weight": drone.weight,
                "price_per_hour": str(drone.price_per_hour),
                "kirala": f'<a href="{request.build_absolute_uri(f"/rental/{drone.id}/")}">Kirala</a>'
            })
        response = {
            "data": data
        }
        return JsonResponse(response)
    else:
        return render(request, 'drones_list.html')

def home(request):
    return render(request, 'home.html')

@login_required
def rental_booking(request, drone_id):
    drone = get_object_or_404(Drone, id=drone_id)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False) #Sadece başlangıç ve bitiş tarihleri olduğu için geçici bir kayıt işlemi yapılır
            rental.user = request.user #Kiralam işlemi için atamalar yapılır
            rental.drone = drone
            rental.save()
            return redirect('drones_list')
    else:
        form = RentalForm()

    return render(request, 'rental_booking.html', {'form': form, 'drone': drone})

@login_required
def delete_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    
    if rental.user != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403) 
    
    rental.drone.availability = True
    rental.drone.save()
    
    rental.delete()
    
    return JsonResponse({'message': 'Rental deleted successfully'}, status=200)


@login_required
def update_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    
    if rental.user != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403) 
    
    if request.method == 'POST':
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            updated_rental = form.save(commit=False)
            updated_rental.user = request.user
            updated_rental.drone = rental.drone 
            updated_rental.save()
            
            return JsonResponse({'message': 'Rental updated successfully'}, status=200)
    else:
        form = RentalForm(instance=rental)
    
    return render(request, 'update_rental.html', {'form': form, 'rental': rental})