
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from home_module.models import HotelRoom, DetailRoom, Reserved


class RoomView(ListView):
    template_name = 'home_module/room_page.html'
    model = HotelRoom


class DetailRoomView(DetailView):
    template_name = 'home_module/detail_room.html'
    model = DetailRoom


class ReservedView(CreateView):
    template_name = 'home_module/reserved.html'
    model = Reserved
    fields = ['date_in', 'date_out']
    success_url = reverse_lazy('home:secsos')

    def form_valid(self, form, *args, **kwargs):
        reserved = form.save(commit=False)
        reserved.user = self.request.user
        reserved.room = DetailRoom.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)





