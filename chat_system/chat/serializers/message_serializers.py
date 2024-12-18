from rest_framework import serializers
from chat.models import Message,Thread

class MessageSerializer(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(), required=False)
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        user_name = attrs.get('user_name')

        # Check for existing user_id and user_name combination
        if Message.objects.filter(user_id=user_id).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError({'user_id': f"User ID '{user_id}' is already associated with a {user_name}."})
        if Message.objects.filter(user_name=user_name).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError({'user_name': f"Username '{user_name}' is already associated with a {user_id}."})

        return attrs
