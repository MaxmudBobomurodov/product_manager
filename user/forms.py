from django import forms
from django.contrib.auth.models import AbstractUser
from django.db.transaction import clean_savepoints

from user.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField()
    password  = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if confirm_password != password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
