from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from chat.models import ThreadParticipant, Thread
from chat.serializers.participant_serializers import ThreadParticipantSerializer

class ThreadParticipantViewSet(viewsets.ModelViewSet):
    queryset = ThreadParticipant.objects.all()
    serializer_class = ThreadParticipantSerializer  # Use a single serializer

    def perform_create(self, serializer):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            try:
                thread = Thread.objects.get(id=thread_id)  # Find the thread by ID
            except Thread.DoesNotExist:
                raise NotFound(detail="Thread not found")  # Raise 404 if the thread doesn't exist

            # Save the participant associated with the thread
            serializer.save(thread=thread)

    # Optionally override get_queryset if you want to filter based on the thread
    def get_queryset(self):
        queryset = super().get_queryset()
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            queryset = queryset.filter(thread_id=thread_id)
        return queryset
