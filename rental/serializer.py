from rest_framework import serializers
from .models import Drone, Rental

#Model verilerine API ile kolayca erişilebilmesi için tasarlanır
class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'