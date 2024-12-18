from rest_framework import viewsets
from chat.models import ThreadParticipant
from chat.serializers.participant_serializers import ThreadParticipantSerializer

class ThreadParticipantViewSet(viewsets.ModelViewSet):
    queryset = ThreadParticipant.objects.all()
    serializer_class = ThreadParticipantSerializer

    def get_queryset(self):
        thread_id = self.kwargs.get("thread_id")
        if thread_id:
            return ThreadParticipant.objects.filter(thread_id=thread_id)
        return super().get_queryset()
