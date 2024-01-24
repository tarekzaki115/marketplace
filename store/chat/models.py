from django.db import models

from user.models import User
from django.db.models import Q


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="sender"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False, related_name="receiver"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=500, blank=False, null=False)
    read = models.BooleanField(default=False)

    @staticmethod
    def get_unread_message_count(pk1, pk2):
        return Message.objects.filter(
            Q(sender_id=pk1, receiver_id=pk2) | Q(sender_id=pk2, receiver_id=pk1)
        ).count()

    @staticmethod
    def get_last_message_in_chat(pk1, pk2):
        return (
            Message.objects.filter(
                Q(sender_id=pk1, receiver_id=pk2) | Q(sender_id=pk2, receiver_id=pk1)
            )
            .select_related("sender", "receiver")
            .order_by("-created_at")
            .first()
        )

    @staticmethod
    def chat_exists(pk1, pk2):
        message = Message.objects.filter(
            Q(sender_id=pk1, receiver_id=pk2) | Q(sender_id=pk2, receiver_id=pk1)
        ).first()
        if message:
            return True
        else:
            return False

    def get_all_messages_in_chat(pk1, pk2):
        messages = Message.objects.filter(
            Q(sender_id=pk1, receiver_id=pk2) | Q(sender_id=pk2, receiver_id=pk1)
        ).order_by("created_at")
        return messages
