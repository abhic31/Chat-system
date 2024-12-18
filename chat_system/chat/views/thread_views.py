from rest_framework import viewsets
from chat.models import Thread
from chat.serializers.thread_serializers import ThreadSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
