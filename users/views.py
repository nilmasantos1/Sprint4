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
