# chat/models.py
from django.db import models
from django.contrib.auth.models import User

# ... keep your existing Todo model if you have one ...

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'