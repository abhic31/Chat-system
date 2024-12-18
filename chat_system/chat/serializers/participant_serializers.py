from rest_framework import serializers
from chat.models import ThreadParticipant

class ThreadParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadParticipant
        fields = '__all__'
