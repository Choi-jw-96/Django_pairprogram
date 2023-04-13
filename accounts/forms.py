from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='닉네임')
    email = forms.EmailField(max_length=254, required=True, label='이메일')
    first_name = forms.CharField(max_length=30, required=True, label='이름')
    last_name = forms.CharField(max_length=30, required=True, label='성씨')
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
