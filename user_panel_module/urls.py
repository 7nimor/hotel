from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('', views.UserPanelDashboard.as_view(), name='user_panel_dashboard'),
    path('edit/<int:pk>/', views.EditUserProfilePage.as_view(), name='edit_user_panel'),
    path('change_pass/<int:pk>/', views.ChangePasswordUser.as_view(), name='change_pass_user')
]
