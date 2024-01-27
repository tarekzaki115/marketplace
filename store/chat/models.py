from django.db import models

from user.models import User
from django.db.models import Q


class Chat(models.Model):
    participent1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="participent1",
    )
    participent2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="participent2",
    )

    @staticmethod
    def get_participents(pk, chats):
        chat_det = {}
        for chat in chats:
            if chat.participent1_id == pk:
                last_message = Message.get_last_message_in_chat(
                    pk, chat.participent2_id
                )
                chat_det[chat.participent2] = last_message

            elif chat.participent2_id == pk:
                last_message = Message.get_last_message_in_chat(
                    pk, chat.participent1_id
                )
                chat_det[chat.participent1] = last_message

        return chat_det

    @staticmethod
    def get_open_chats(pk):
        chats = Chat.objects.filter(Q(participent1_id=pk) | Q(participent2_id=pk))
        # print(chats)
        chat_det = Chat.get_participents(pk, chats)
        return chat_det


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
        if not message:
            return False
        else:
            return True

    def get_all_messages_in_chat(pk1, pk2):
        messages = Message.objects.filter(
            Q(sender_id=pk1, receiver_id=pk2) | Q(sender_id=pk2, receiver_id=pk1)
        ).order_by("created_at")
        return messages
