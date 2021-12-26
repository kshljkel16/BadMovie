from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('success_registration/', SuccessfulRegistrationView.as_view(), name='success-registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]