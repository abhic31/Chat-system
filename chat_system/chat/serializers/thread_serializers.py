from rest_framework import serializers
from chat.models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Thread
        fields = '__all__'

    def validate(self, attrs):
        """
        Ensure each entity_type can have only one entity_id.
        """
        entity_type = attrs.get('entity_type')
        entity_id   = attrs.get('entity_id')

        # duplicates check
        if Thread.objects.filter(entity_type=entity_type, entity_id=entity_id).exists():
            raise serializers.ValidationError(
                {"detail": f"Entity type '{entity_type}' already has entity ID '{entity_id}'. Duplicates are not allowed."}
            )
        return attrs