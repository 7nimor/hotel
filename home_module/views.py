from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from account_module.models import User
from home_module.models import HotelRoom, DetailRoom, Reserved



class RoomView(ListView):
    template_name = 'home_module/room_page.html'
    model = HotelRoom



def detail_room(request, detail):
    room_hotel = DetailRoom.objects.get(pk=detail)
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        hotel = DetailRoom.objects.get(pk=detail)
        user = User.objects.filter(id=request.user.id)
        if user:

            room_hotel.Reservation = True
            room_hotel.save()
            Reserved.objects.create(room=hotel, user=request.user, date_in=checkin
                                    , date_out=checkout)

            return redirect(reverse('secsos'))
        else:
            return redirect(reverse('register_page'))
    context = {
        'detail_room': room_hotel,
    }

    return render(request, 'home_module/detail_room.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('room'))


def secsos(request):
    return render(request, 'home_module/seccsos.html')
