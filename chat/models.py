from django.db import models
from django.contrib.auth.models import User



class Inbox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.__str__()


class Chat(models.Model):
    sender = models.ForeignKey(User, null=False, blank=False, related_name='sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, null=False, blank=False, related_name='reciever', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.reciever.__str__()

class Message(models.Model):
    chat = models.ForeignKey(Chat, null=False, blank=False, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)