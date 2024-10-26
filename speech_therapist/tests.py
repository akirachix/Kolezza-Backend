from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Speech_Therapist
from users.models import User

class SpeechTherapistModelTest(TestCase):

    def setUp(self):
        #User instance for the Speech Therapist
        self.user = User.objects.create(
            username="therapist1",
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            role="speech_therapist"
        )

        # Speech Therapist record (Happy path setup)
        self.speech_therapist = Speech_Therapist.objects.create(
            user=self.user,
            hospital_name="General Hospital",
            is_deleted=False
        )

    def test_create_speech_therapist(self):
        """Test creating a valid Speech Therapist record."""
        # Create another User instance
        user = User.objects.create(
            username="therapist2",
            first_name="Jane",
            last_name="Smith",
            email="janesmith@example.com",
            role="speech_therapist"
        )

        speech_therapist = Speech_Therapist.objects.create(
            user=user,
            hospital_name="City Hospital",
            is_deleted=False
        )

        self.assertEqual(speech_therapist.hospital_name, "City Hospital")
        self.assertFalse(speech_therapist.is_deleted)
        self.assertEqual(speech_therapist.user.username, "therapist2")

    def test_soft_delete_speech_therapist(self):
        """Test soft deleting a Speech Therapist record."""
        self.speech_therapist.soft_delete()

        # After soft deletion, is_deleted should be True, and deleted_at should be set
        self.assertTrue(self.speech_therapist.is_deleted)
        self.assertIsNotNone(self.speech_therapist.deleted_at)
        self.assertEqual(self.speech_therapist.__str__(), "General Hospital - Deleted")

    def test_hospital_name_cannot_be_empty(self):
        """Test that hospital_name cannot be empty (unhappy path)."""
        speech_therapist = Speech_Therapist(
            user=self.user,  
            hospital_name="",  
            is_deleted=False
        )
        with self.assertRaises(ValidationError):
            speech_therapist.clean()  

    def test_speech_therapist_str_method(self):
        """Test the string representation of the Speech Therapist model."""
        self.assertEqual(str(self.speech_therapist), "General Hospital - Active")
        self.speech_therapist.soft_delete()
        self.assertEqual(str(self.speech_therapist), "General Hospital - Deleted")
