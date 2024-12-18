from rest_framework import viewsets
from chat.models import Message, Thread
from chat.serializers.message_serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            return Message.objects.filter(thread_id=thread_id)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            try:
                thread = Thread.objects.get(id=thread_id)  # Ensure the thread exists
            except Thread.DoesNotExist:
                raise NotFound(detail="Thread not found")  # Raise a 404 if thread does not exist
            
            # Save the message associated with the found thread
            serializer.save(thread=thread)
