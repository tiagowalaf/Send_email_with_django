from django.shortcuts import render, redirect
from register.forms.register_class import Register
from django.views.decorators.http import require_POST, require_GET
from django.core.mail import send_mail
import random

@require_GET
def home_create_user(request):
    session_user = request.session.get('session_user', None)
    form_register = Register(session_user)
    _context = {'form':form_register}
    return render(request, 'register/cadastro.html',_context)
@require_POST
def create_user(request):
    lista = set()
    while len(lista) < 4:
        a = random.randint(0, 99)
        lista.add(str(a))
    convert = "".join(lista)
    session_key = request.session['session_user'] = request.POST.dict()
    form_register = Register(session_key)
    if form_register.is_valid():
        email_ = form_register.cleaned_data.get('email', None)
        send_mail(
            subject='Seu código de verificação',
            message='',
            html_message=f'''
            <div style="width: 100vw;
                height: 50vh;
                text-align: center;">
                <p style="font-family: sans-serif; font-size: 1.5rem; color: black;" class="pp">
                    Copie o código abaixo e cole na tela do token:
                </p>
        
                <p style="font-family: sans-serif;">
                    <h3 style="font-size: 1.2rem">{convert}</h3>
                </p>
                <footer style="font-family: sans-serif; margin-top: 100px;">
                    Copyright © 2024 Raffles One, All rights reserved.
                </footer>
            </div>
            ''',
            from_email='bussinessdownload@gmail.com',
            recipient_list=[email_]
            )
        token_key = request.session['token_uuid_key'] = convert
        return redirect('register:show_template_token')
    else:
        return redirect('register:cad_home')

# Aqui fazemos o envio de emails, usando alguns parâmetros, mas é possível não usá-los.