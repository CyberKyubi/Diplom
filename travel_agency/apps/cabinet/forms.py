from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Имя'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Повторите пароль'})

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Почта'}))

    class Meta:
        model = User
        fields = ("username", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Имя'})
        self.fields['username'].label = False
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль'})
        self.fields['password'].label = False

    class Meta:
        model = User
        fields = ['username', 'password']

