from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from account.tasks import send_activation_mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(min_length=8,
                               widget=forms.PasswordInput,
                               required=True)
    password_confirm = forms.CharField(min_length=8,
                               widget=forms.PasswordInput,
                               required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь уже зарегестрирован')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password != password_confirm:
            print('PPPPPPPPPPPP')
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        user = User.objects.create(**self.cleaned_data)
        print(dir(user))
        user.create_activation_code()
        send_activation_mail.delay(user.email, user.activation_code)
        return user

