from django.test import TestCase
from chat.models import Thread, ThreadParticipant

class ThreadParticipantModelTests(TestCase):
    def setUp(self):
        self.thread = Thread.objects.create(
            entity_type = "ORDER",
            title       = "Test Thread"
        )

    def test_add_participant(self):
        """Test adding a participant to a thread."""
        participant = ThreadParticipant.objects.create(
            thread    = self.thread,
            user_id   = "123e4567-e89b-12d3-a456-426614174000",
            user_name = "Test User"
        )
        self.assertEqual(participant.user_name, "Test User")

    def test_get_participant(self):
        """Test retrieving a participant from a thread using get()."""
        participant = ThreadParticipant.objects.create(
            thread    = self.thread,
            user_id   = "123e4567-e89b-12d3-a456-426614174000",
            user_name = "Test User"
        )
        retrieved_participant = ThreadParticipant.objects.get(user_id="123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(retrieved_participant.user_name, "Test User")