from django.db import models

from user.models import User


class Chat(models.Model):
    particepent_1 = models.ForeignKey(User, blank=False, Null=False)
    particepent_2 = models.ForeignKey(User, blank=False, Null=False)


class Message(models.Model):
    sender = models.ForeignKey(User, blank=False, Null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, blank=False, Null=False)
    body = models.CharField(max_length=500, blank=False, Null=False)
