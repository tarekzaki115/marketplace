from django.db import models

from user.models import User

"""
class Chat(models.Model):
    particepent_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="userOne"
    )
    particepent_2 = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="userTwo"
    )
"""


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="sender"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="receiver"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=500, blank=False, null=False)

    def get_messages(pk1, pk2):
        messages = []
        messages1 = Message.objects.filter(sender_id=pk1, receiver_id=pk2)
        messages2 = Message.objects.filter(sender_id=pk2, receiver_id=pk1)
        for x in range(len(messages1)):
            messages.append(messages1[x])

        for x in range(len(messages2)):
            messages.append(messages2[x])

        messages.sort(key=lambda x: x.created_at)
        return messages
