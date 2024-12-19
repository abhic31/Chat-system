from rest_framework import viewsets
from chat.models import Message, Thread
from chat.serializers.message_serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset         = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            return Message.objects.filter(thread_id=thread_id)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            thread = Thread.objects.get(id=thread_id)  
            serializer.save(thread=thread)
