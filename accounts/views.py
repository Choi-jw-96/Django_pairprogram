from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = AuthenticationForm(request ,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user)
            return redirect('reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
      }
    return render(request, 'accounts/login.html', context)