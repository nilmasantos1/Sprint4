from django.shortcuts import render, redirect
from .forms import UserForm

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Exemplo com vulnerabilidade de Mass Assignment
            return redirect('create_user')  # Redireciona para evitar reenvio do form
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

        # O método 'form.save()' salva os dados diretamente no banco de dados sem realizar validações específicas sobre quais
        # campos o usuário pode modificar. Se o formulário incluir campos sensíveis como 'is_admin', isso pode permitir que
        # o usuário altere valores que não deveria, como se promover a administrador.
        
        # Mitigação: A forma correta de evitar essa vulnerabilidade é garantir que campos como 'is_admin' não sejam
        # acessíveis no formulário ou realizar validações adicionais no backend para garantir que apenas dados permitidos
        # sejam salvos.