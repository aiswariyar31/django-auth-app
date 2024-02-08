from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')
