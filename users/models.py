
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
