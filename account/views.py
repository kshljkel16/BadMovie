from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from account.forms import *
from movie.models import Movie

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'movie/signup.html'
    success_url = reverse_lazy('success-registration')


class SuccessfulRegistrationView(TemplateView):
    template_name = 'movie/success_registration.html'


# http://127.0.0.1:8000/account/activate/?u=24weaf25
class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        print(code)
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()

        return render(request, 'movie/activation.html', {})


class SignInView(LoginView):
    template_name = 'movie/login.html'
    success_url = '/'


class LogOutView(LogoutView):
    LOGOUT_REDIRECT_URL = '/'