from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
