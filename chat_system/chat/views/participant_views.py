from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from chat.models import ThreadParticipant, Thread
from chat.serializers.participant_serializers import ThreadParticipantSerializer,ThreadGetParticipantSerializer

class ThreadParticipantViewSet(viewsets.ModelViewSet):
    queryset = ThreadParticipant.objects.all()

    def get_serializer_class(self):
        # Use the appropriate serializer for each action (GET or POST)
        if self.action == 'list':  # GET request to list participants
            return ThreadGetParticipantSerializer
        return ThreadParticipantSerializer  # POST or other methods

    def perform_create(self, serializer):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            try:
                thread = Thread.objects.get(id=thread_id)  # Ensure the thread exists
            except Thread.DoesNotExist:
                raise NotFound(detail="Thread not found")  # Raise 404 if thread does not exist

            # Save the participant associated with the thread
            serializer.save(thread=thread)
