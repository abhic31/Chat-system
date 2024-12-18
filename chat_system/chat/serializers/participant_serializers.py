from rest_framework import serializers
from chat.models import ThreadParticipant,Thread,Message

class ThreadParticipantSerializer(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(), required=False)
    class Meta:
        model = ThreadParticipant
        fields = '__all__'

    def validate(self, attrs):
        user_name = attrs.get('user_name')
        user_id = attrs.get('user_id')
        thread = attrs.get('thread')

        # Validate unique user_name and user_id combination
        if ThreadParticipant.objects.filter(user_name=user_name, user_id=user_id).exists():
            raise ValidationError(f"A participant with user_name '{user_name}' and user_id '{user_id}' already exists.")
        
        return attrs

