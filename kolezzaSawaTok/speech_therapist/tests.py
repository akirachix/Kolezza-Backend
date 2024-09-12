from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Speech_Therapist

class SpeechTherapistModelTest(TestCase):

    def setUp(self):
        # Set up a valid Speech Therapist record (Happy path setup)
        self.speech_therapist = Speech_Therapist.objects.create(
            hospital_name="General Hospital",
            is_deleted=False
        )

    # Test case for the happy path (valid therapist creation)
    def test_create_speech_therapist(self):
        """Test creating a valid Speech Therapist record."""
        speech_therapist = Speech_Therapist.objects.create(
            hospital_name="City Hospital",
            is_deleted=False
        )
        self.assertEqual(speech_therapist.hospital_name, "City Hospital")
        self.assertFalse(speech_therapist.is_deleted)

    # Test case for soft deletion (happy path)
    def test_soft_delete_speech_therapist(self):
        """Test soft deleting a Speech Therapist record."""
        self.speech_therapist.soft_delete()
        
        # After soft deletion, is_deleted should be True, and deleted_at should be set
        self.assertTrue(self.speech_therapist.is_deleted)
        self.assertIsNotNone(self.speech_therapist.deleted_at)
        self.assertEqual(self.speech_therapist.__str__(), "General Hospital - Deleted")

    # Test case for ValidationError (unhappy path)
    def test_hospital_name_cannot_be_empty(self):
        """Test that hospital_name cannot be empty (unhappy path)."""
        speech_therapist = Speech_Therapist(
            hospital_name="",  # Invalid, as hospital_name cannot be empty
            is_deleted=False
        )
        with self.assertRaises(ValidationError):
            speech_therapist.clean()  # This should raise ValidationError

    # Test case for the str method (happy path)
    def test_speech_therapist_str_method(self):
        """Test the string representation of the Speech Therapist model."""
        self.assertEqual(str(self.speech_therapist), "General Hospital - Active")
        self.speech_therapist.soft_delete()
        self.assertEqual(str(self.speech_therapist), "General Hospital - Deleted")
