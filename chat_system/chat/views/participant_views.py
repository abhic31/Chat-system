from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from chat.models import ThreadParticipant, Thread
from chat.serializers.participant_serializers import ThreadParticipantSerializer

class ThreadParticipantViewSet(viewsets.ModelViewSet):
    queryset         = ThreadParticipant.objects.all()
    serializer_class = ThreadParticipantSerializer 

    def perform_create(self, serializer):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            try:
                thread = Thread.objects.get(id=thread_id)  
            except Thread.DoesNotExist:
                raise NotFound(detail="Thread not found")  
            serializer.save(thread=thread)

    def get_queryset(self):
        queryset  = super().get_queryset()
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            queryset = queryset.filter(thread_id=thread_id)
        return queryset
