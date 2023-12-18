from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.RoomView.as_view(), name='room'),
    path('<int:pk>', views.DetailRoomView.as_view(), name='detail_room'),
    path('reserved/<int:pk>/',views.ReservedView.as_view(),name='reserved')

]
