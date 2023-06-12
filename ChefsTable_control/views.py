from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm, Booking
from .models import Cuisine, Menu
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation
# Create your views here.

def form_view(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("Reservation Success!")

    else :    
        context = {"form": form}
        return render(request, "booking.html", context)

@method_decorator(csrf_exempt, name='dispatch')
class BookingsView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        exist = Reservation.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if not exist:
            booking = Reservation.objects.create(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            return Response({'success': True})
        else:
            return Response({'error': 'Booking already exists.'}, status=400)
        
    def get(self, request, *args, **kwargs):
        date = request.GET.get('date', timezone.now().date())
        bookings = Booking.objects.filter(reservation_date=date)
        booking_json = serializers.serialize('json', bookings)
        return Response(booking_json, content_type='application/json')


def home(request):
    return render(request,'home.html')


def about(request):
    #about_content = {'about' : "Order food online and get it delivered to you Hot and fresh at your doorstep!"}
    return render(request,"about.html")

def menu(request):
    cuisines = Cuisine.objects.all()
    menus = Menu.objects.all()
    context = {'cuisines': cuisines, 'menus': menus}
    return render(request, 'menu.html', context)

def reservation(request):
    form = Booking()
    if request.method == "POST":
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"sucessbook.html",{"form": form, 'successful_submit': False} )
        
    context = {"form": form, 'successful_submit': False}
    return render(request, "booking.html", context)
