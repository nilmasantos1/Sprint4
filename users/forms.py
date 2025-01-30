from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_admin'] 
# A inclusão do campo 'is_admin' no formulário permite que qualquer usuário possa modificar o seu status de administrador.
        # Isso é uma vulnerabilidade, pois um atacante pode alterar esse campo e se promover a administrador do sistema, 
        # o que não é desejado. O campo 'is_admin' deve ser controlado apenas no backend e não deve ser acessível a usuários comuns.
        
        # Mitigação: Para evitar essa vulnerabilidade, é importante excluir o campo 'is_admin' do formulário.
        # Isso pode ser feito removendo 'is_admin' da lista de campos, como mostrado abaixo:

        # fields = ['username', 'email']  # Remover 'is_admin' da lista de campos acessíveis no formulário