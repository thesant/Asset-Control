import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$')

    if not regex.match(password):
        raise ValidationError((
            'Definir mensagem de password fraco'
        ),
            code='Invalid'
        )


def addplaceholder(fields, valPlaceholder):
    fields.widget.attrs['placeholder'] = valPlaceholder


class UserRegisterForm(forms.ModelForm):

    # Sobscrever campo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs['placeholder']= 'type your first name'
        addplaceholder(self.fields['first_name'], 'type your name')
        addplaceholder(self.fields['last_name'], 'type your last name')
        addplaceholder(self.fields['username'], 'type your username')
        addplaceholder(self.fields['email'], 'type your E-mail')

    # Add field
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeHolder': 'Repeat your password'
            }),
        validators=[strong_password]
    )

    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

        help_texts = {
            'last_name': 'Sobrenome',
            'email': 'Email valido'
        }

        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Your password'
            })
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            if password != password2:
                raise ValidationError({
                    'password': 'Senhas não identicas'
                })


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter your username...',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Password'
            }
        )
    )
