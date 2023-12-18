from django.urls import path
from . import views


app_name = 'register'
urlpatterns = [
    path('', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('about', views.StaffView.as_view(), name='about'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),

    # path('logout', views.LogoutView.as_view(), name='logout_page'),
    # path('forget_pass', views.ForgetPassword.as_view(), name='forget_page'),
    # path('activate/<email_active_code>', views.ActivateView.as_view(), name='activate_email'),
    # path('reset/<active_code>', views.ResetPassword.as_view(), name='reset_pass'),
]
