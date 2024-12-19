from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from chat.models import Thread, ThreadParticipant, Message
import uuid

class ThreadAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.thread_url = reverse("thread-list")
        self.thread = Thread.objects.create(id=uuid.uuid4())

    def test_get_threads(self):
        response = self.client.get(self.thread_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_thread(self):
        data = {"title": "New Thread","entity_type":"STOCK"}
        response = self.client.post(self.thread_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Thread")
