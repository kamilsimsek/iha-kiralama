from django.contrib import admin
from .models import Drone, Rental

#drone ve rental modellerini admin panelde erişilebilir duruma getiriyoruz
admin.site.register(Drone)
admin.site.register(Rental)