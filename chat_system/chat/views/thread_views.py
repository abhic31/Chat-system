from rest_framework import viewsets
from chat.models import Thread
from chat.serializers.thread_serializers import ThreadSerializer
from django.db.models import Q
from django.http import Http404

class ThreadViewSet(viewsets.ModelViewSet):
    queryset         = Thread.objects.all()
    serializer_class = ThreadSerializer

    def get_queryset(self):

        queryset    = super().get_queryset()
        entity_type = self.request.query_params.get('entity_type')
        entity_id   = self.request.query_params.get('entity_id')
        thread_id   = self.kwargs.get('thread_id')

        # Build the filter dynamically using Q
        query_filter = Q()
        if entity_type:
            query_filter &= Q(entity_type=entity_type)
        if thread_id:
            query_filter &= Q(id=thread_id)
        if entity_id:
            if not Thread.objects.filter(entity_id=entity_id).exists():
                raise Http404(f"Entity with ID '{entity_id}' does not exist.")
            query_filter &= Q(entity_id=entity_id)

        if query_filter:
            queryset = queryset.filter(query_filter)
        return queryset
