from rest_framework import serializers
from chat.models import Message,Thread
from chat.serializers.participant_serializers import ThreadParticipantBasicSerializer 

class MessageSerializer(serializers.ModelSerializer):
    thread      = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(), required=False)
    class Meta:
        model  = Message
        fields = '__all__'






