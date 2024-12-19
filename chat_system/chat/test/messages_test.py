from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Thread, ThreadParticipant, Message
import uuid

class MessageAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.thread = Thread.objects.create(id=uuid.uuid4(), name="Test Thread")
        self.participant = ThreadParticipant.objects.create(
            thread=self.thread, user_name="test_user"
        )
        self.message = Message.objects.create(
            thread=self.thread,
            participant=self.participant,
            content="Test message 444",
        )
        self.thread_id = self.thread.id
        self.messages_url = reverse("messages-list", kwargs={"thread_id": self.thread_id})

    def test_get_messages(self):
        response = self.client.get(self.messages_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test message", response.data[0]["content"])

    def test_create_message(self):
        data = {
            "participant": str(self.participant.id),
            "content": "New test message",
        }
        response = self.client.post(self.messages_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["content"], "New test message")
        self.assertEqual(response.data["participant"], str(self.participant.id))


