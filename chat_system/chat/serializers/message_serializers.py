from rest_framework import serializers
from chat.models import Message,Thread

class MessageSerializer(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(), required=False)
    class Meta:
        model  = Message
        fields = '__all__'

