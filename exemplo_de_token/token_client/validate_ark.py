from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from register.forms.code_unique import CodeUniqueToken
from django.views.decorators.http import require_POST, require_GET
from register.forms.register_class import Register

@require_GET
def show_template_token(request):
    token_uuid_k = request.session.get('token_uuid_key', '')
    if not token_uuid_k:
        return HttpResponse('Token não existe')
    else:
        form_ = CodeUniqueToken()
        context_ = {'form_token':form_}
        return render(request, 'confirmation/confirmation.html', context_)

@require_POST
def validate_token_if_true(request):
    session_key = request.session.get('session_user', '')
    if not session_key:
        raise Http404('Sessão não encontrada')
    form_register = Register(session_key)
    token_session = request.POST.get('token_send','')
    token_uuid_k = request.session.get('token_uuid_key', '')
    if token_session == token_uuid_k and form_register.is_valid():
        del request.session['session_user']
        del request.session['token_uuid_key']
        if form_register.is_valid():
            user = form_register.save(commit=False)
            user.set_password(user.password)
            form_register.save()
            return redirect('register:login')
    else:
        raise Http404('Token inválido')