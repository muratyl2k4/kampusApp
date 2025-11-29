from django.db import models
from accounts.models import KampusUser

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(KampusUser, related_name='chatrooms')

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(KampusUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    