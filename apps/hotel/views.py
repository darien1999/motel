from django.shortcuts import render
from django.http import HttpResponse
from apps.hotel.forms import hotelForm
# Create your views here.


def index(request):
    return render(request, 'hotel/index.html')


def hotel_view(request):
    if request.method == 'POST':
        form = hotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel:index')
    else:
        form = hotelForm()
    return render(request, 'hotel/hotel_form.html', {'form':form})


def registro(request):
    return render(request,'hotel/registro.html')

def boot(request):
    return render(request,'hotel/boot.html')

def principal(request):
    return render(request,'hotel/Principal.html')