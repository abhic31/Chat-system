from rest_framework import serializers
from chat.models import ThreadParticipant,Thread,Message

class ThreadParticipantSerializer(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(), required=False)
    class Meta:
        model = ThreadParticipant
        fields = '__all__'

class ThreadGetParticipantSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = ThreadParticipant
        fields = ['user_id', 'user_name']

    def get_user_name(self, obj):
        latest_message = Message.objects.filter(
            thread=obj.thread, user_id=obj.user_id
        ).order_by('-created_at').first()

        # Return the user_name from the latest message, or None if no messages exist
        return latest_message.user_name if latest_message else None