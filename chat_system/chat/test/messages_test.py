from django.test import TestCase
from chat.models import Thread, ThreadParticipant, Message
import uuid

class MessageModelTests(TestCase):
    def setUp(self):
        self.thread = Thread.objects.create(
            entity_type = "ORDER",
            title       = "Test Thread"
        )
        # Create a participant for the thread
        self.participant = ThreadParticipant.objects.create(
            thread    = self.thread,
            user_id   = uuid.uuid4(),
            user_name = "Test User"
        )

    def test_create_message(self):
        """Test creating a message and associating it with a thread and participant."""
        message_content = "This is a test message"
        # Create a message
        message = Message.objects.create(
            thread      = self.thread,
            participant = self.participant,
            content     = message_content
        )
        self.assertEqual(message.content, message_content)
        self.assertEqual(message.thread, self.thread)
        self.assertEqual(message.participant, self.participant)
        self.assertIsNotNone(message.created_at)

    def test_message_association_with_thread(self):
        """Test that a message is correctly associated with its thread."""
        message = Message.objects.create(
            thread=self.thread,
            participant=self.participant,
            content="Test message"
        )
        messages = self.thread.messages.all()
        self.assertIn(message, messages)

    def test_message_association_with_participant(self):
        """Test that a message is correctly associated with its participant."""
        message = Message.objects.create(
            thread=self.thread,
            participant=self.participant,
            content="Test message"
        )
        messages = self.participant.messages.all()
        self.assertIn(message, messages)
