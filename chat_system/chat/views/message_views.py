from rest_framework import viewsets
from chat.models import Message
from chat.serializers.message_serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            return Message.objects.filter(thread_id=thread_id)
        return super().get_queryset()
