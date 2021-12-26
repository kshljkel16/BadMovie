from .utils import send_activation_code
from cinema.celery import app


@app.task
def send_activation_mail(email, activation_code):
    send_activation_code(email,activation_code)
