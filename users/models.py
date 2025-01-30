
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
# O campo 'is_admin' é vulnerável a ataques de Mass Assignment. Se o formulário associado a este modelo permitir
    # que um usuário modifique o campo 'is_admin', isso pode permitir que um atacante se promova a um status de administrador,
    # o que não deveria ser permitido.
    
    # Mitigação: Para proteger o campo 'is_admin', é recomendável não incluir este campo no formulário que o usuário utiliza,
    # ou realizar uma verificação rigorosa no backend antes de permitir que o valor seja alterado.
    def __str__(self):
        return self.username
