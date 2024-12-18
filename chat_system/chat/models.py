from django.db import models
import uuid


ENTITY_TYPES = [
    ("ORDER", "Order"),
    ("ORDERLINE", "Order Line"),
    ("SUPPLIER", "Supplier"),
    ("PAYMENT", "Payment"),
    ("STOCK", "Stock Item"),
]
class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPES) 
    entity_id = models.UUIDField(default=uuid.uuid4)  
    title = models.TextField()  # Thread title
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        indexes = [
            models.Index(fields=["entity_type", "entity_id"]),  # Composite index for entity_type and entity_id
        ]

    def __str__(self):
        return f"{self.entity_type} - {self.title}"

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thread = models.ForeignKey(Thread, related_name="messages", on_delete=models.CASCADE)
    user_id = models.UUIDField(default=uuid.uuid4)
    user_name = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'user_name'], name='unique_user_id_user_name')
        ]

    def __str__(self):
        return f"{self.user_name} - {self.content[:20]}"



class ThreadParticipant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thread = models.ForeignKey(Thread, related_name="participants", on_delete=models.CASCADE)
    user_id = models.UUIDField()
