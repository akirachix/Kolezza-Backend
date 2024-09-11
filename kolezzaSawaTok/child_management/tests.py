from django.test import TestCase
from django.utils import timezone
from child_module.models import ChildModule
from level_of_stuttering.models import LevelOfStuttering
from .models import Child_Management
from datetime import date

class ChildManagementTestCase(TestCase):
    def setUp(self):
        # Create a sample Level of Stuttering record
        self.level_of_stuttering = LevelOfStuttering.objects.create(
            type_of_stuttering="Developmental",
            description="Stuttering that develops in early childhood",
            duration=timezone.timedelta(weeks=2)
        )
        # Create a sample Child Module record
        self.child_module = ChildModule.objects.create(
            name="Speech Therapy Module",
            description="Module for speech therapy",
            duration=timezone.timedelta(weeks=4),
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering
        )
        # Create a sample Child record
        self.child = Child_Management.objects.create(
            first_name="Jane",
            last_name="Doe",
            middle_name="A.",
            gender="Female",
            date_of_birth=date(2018, 1, 1),
            level_of_stuttering_id=self.level_of_stuttering,  # Correct field name
            childmodule_id=self.child_module  # Correct field name
        )

    # Happy Path Tests
    def test_child_creation(self):
        """Test that a child record is correctly created."""
        self.assertEqual(self.child.first_name, "Jane")
        self.assertEqual(self.child.last_name, "Doe")
        self.assertEqual(self.child.middle_name, "A.")
        self.assertEqual(self.child.gender, "Female")
        self.assertEqual(self.child.date_of_birth, date(2018, 1, 1))
        self.assertEqual(self.child.level_of_stuttering_id, self.level_of_stuttering)
        self.assertEqual(self.child.childmodule_id, self.child_module)
        self.assertFalse(self.child.is_deleted)

    def test_soft_delete(self):
        """Test that the soft delete functionality works correctly."""
        self.child.soft_delete()
        # Check that the record is marked as deleted
        self.assertTrue(self.child.is_deleted)
        # Check that updated_at is set correctly
        self.assertIsNotNone(self.child.updated_at)
        # Check if the updated_at time is close to now (with a small delta tolerance)
        self.assertAlmostEqual(self.child.updated_at, timezone.now(), delta=timezone.timedelta(seconds=1))

    # Unhappy Path Tests
def test_invalid_child_creation(self):
    """Test that invalid child data raises validation errors."""
    with self.assertRaises(ValueError):
        # Assume first_name is required and should not be empty
        Child_Management.objects.create(
            first_name="",  # Invalid (empty) first name
            last_name="Doe",
            middle_name="A.",
            gender="Female",
            date_of_birth=date(2018, 1, 1),
            level_of_stuttering_id=self.level_of_stuttering,
            childmodule_id=self.child_module
        )