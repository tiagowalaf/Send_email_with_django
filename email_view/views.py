from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm

def mostrar_form(request):
    contact_form = ContactForm()
    return render(request, 'contact.html',context={'form':contact_form})

def enviar_email(request):
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        message = contact_form.cleaned_data.get("message")
        send_mail(
            subject=subject,  # Assunto da mensagem (Título)
            message=message,  # Mensagem a ser enviada
            from_email=email,  # Email do remetente(seu email)
            recipient_list=['teste@gmail.com'],  # Email do destinatário(para quem?)
        )
    return HttpResponse('Tudo certo')

# Ao usar um parâmetro nomeado, precisaremos nomear os outros também,
# abaixo temos o link da documentação.
# https://docs.djangoproject.com/en/5.0/topics/email/#quick-example