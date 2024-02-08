from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from django.urls import reverse
from accounts.formss import UserCreationForm


# Create your views here.
def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            print('Successfully registered')

            return redirect(reverse('register'))
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            print('login')
            return redirect('register')

    else:
        forms = AuthenticationForm()
    return render(request, 'accounts/login.html', {'forms': forms})
