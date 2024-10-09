from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Seu Email"}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Titulo Mensagem"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Assunto"}))
    
# Este formulário foi criado para podermos digitar nos campos e enviar o email.
# A lógica para usar em um crud seria a mesma.