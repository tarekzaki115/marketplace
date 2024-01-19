from django.db import models

from user.models import User

class Chat(models.Model):
	particepent_1 = Model.Foriegnkey(User, blank= False, Null=False)
	particepent_2 = Model.Foriegnkey(User, blank= False, Null=False)
	
	
	
class Message(models.Model):
	sender = Model.Foriegnkey(User, blank= False, Null=False)
	 created_at = models.DateTimeField(auto_now_add=True)
	 chat = Model.Foriegnkey(Chat, blank= False, Null=False)
	 body = Model.Charfield(max_length=500, blank=False, Null=False)