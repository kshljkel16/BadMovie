from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    message = f'Вы успешно прошли рег. http://127.0.0.1:8000/accounts/activation/?u={activation_code}'
    send_mail('Активация юзера', message, 'elinalen16@gmail.com',[email])