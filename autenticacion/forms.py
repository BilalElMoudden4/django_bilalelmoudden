from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
