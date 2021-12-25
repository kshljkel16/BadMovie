from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from cinema.celery import app

User = get_user_model()

@app.task
def send_activation_mail(email, activation_code):
    message = f'http://127.0.0.1:8000/accounts/activation/?u={activation_code}'
    send_mail('Account activation', message, 'test@gmail.com', [email])