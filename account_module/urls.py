from django.urls import path
from . import views


app_name = 'register'
urlpatterns = [
    path('', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.UserLoginView.as_view(), name='login_page'),
    path('about/', views.StaffView.as_view(), name='about'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),

]
