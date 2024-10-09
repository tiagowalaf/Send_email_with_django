from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import validate_email
from django.urls import reverse

class Register(forms.ModelForm):
    username = forms.CharField(
        required=True,
        max_length=50, widget=forms.TextInput(
        attrs={'class':'input_form_cad','placeholder':'Nome'}),
        error_messages={'invalid':'Usuário inválido'})

    email = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(attrs={'class':'input_form_cad','placeholder':'Email'}),
        error_messages={'invalid': 'Email inválido'},
        validators = [validate_email],)

    password = forms.CharField(
        required=True, 
        max_length=254,
        widget=forms.PasswordInput(attrs={'class':'input_form_cad','placeholder':'Senha'}),
        error_messages={'required':'Campo obrigatório'})

    class Meta:
        model = User
        fields = ['username','email','password']
        
    def get_url_create_user(self, *args, **kwargs):
        return reverse('register:create_user')

    def get_url_login(self, *args, **kwargs):
        return reverse('register:login')

    def clean_username(self):
        _username = self.cleaned_data.get('username', None)
        _exist = User.objects.filter(username=_username).exists()
        if _exist:
            raise ValidationError('Usuário inválido', code='invalid')
        if len(_username) < 5 or len(_username) > 50:
            raise ValidationError('Usuário inválido', code='invalid')
        return _username
    
    def clean_email(self):
        _email = self.cleaned_data.get('email', None)
        _exist = User.objects.filter(email=_email).exists()
        if _exist:
            raise ValidationError('', code='invalid')
        return _email
    
    def clean_password(self):
        _password = self.cleaned_data.get('password', None)
        if not _password:
            raise ValidationError('',code='invalid')
        if len(_password) < 5 or len(_password) > 254:
            raise ValidationError('Senha inválida', code='invalid')
        return _password