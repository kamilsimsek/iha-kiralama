# users/views.py
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rental.models import Rental  # Rental modelini içe aktarıyoruz

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hesabınız oluşturuldu, giriş yapabilirsiniz')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('drones_list')
                else:
                    messages.info(request, 'Kullanıcı aktif değil')
            else:
                messages.info(request, 'Giriş bilgilerinizi kontrol ediniz')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def user_profile(request):
    user = request.user
    rentals = Rental.objects.filter(user=user).select_related('drone')
    return render(request, 'profile.html', {'user': user, 'rentals': rentals})
