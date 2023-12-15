from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomView.as_view(), name='room'),
    path('<int:detail>', views.detail_room, name='detail_room'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('secsos', views.secsos, name='secsos'),

]
