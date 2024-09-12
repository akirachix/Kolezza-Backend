from django.test import TestCase
from .models import Guardian

class GuardianManagerTestCase(TestCase):

    def setUp(self):
        # Set up initial test data
        Guardian.objects.create(first_name='John', middle_name='M.', last_name='Doe', phone_number='1234567890', address='123 Main St')
        Guardian.objects.create(first_name='Jane', middle_name='N.', last_name='Doe', phone_number='0987654321', address='456 Main St', is_active=False)

    def test_get_queryset_only_active(self):
        """Test that get_queryset() only returns active guardians."""
        active_guardians = Guardian.objects.all()
        self.assertEqual(active_guardians.count(), 1)
        self.assertEqual(active_guardians.first().first_name, 'John')

    def test_all_with_deleted(self):
        """Test that all_with_deleted() returns all guardians, including inactive ones."""
        all_guardians = Guardian.objects.all_with_deleted()
        self.assertEqual(all_guardians.count(), 2)
        self.assertIn('John', [guardian.first_name for guardian in all_guardians])
        self.assertIn('Jane', [guardian.first_name for guardian in all_guardians])

    def test_soft_delete(self):
        """Test that soft_delete() marks a guardian as inactive."""
        guardian = Guardian.objects.get(first_name='John')
        guardian.soft_delete()
        self.assertFalse(guardian.is_active)

        # Check that the guardian does not appear in the default queryset anymore
        active_guardians = Guardian.objects.all()
        self.assertEqual(active_guardians.count(), 0)

def test_save_guardian(self):
    """Test that save_guardian() properly saves a guardian."""
    # Use all_with_deleted() to include inactive guardians in the query
    guardian = Guardian.objects.all_with_deleted().get(first_name='Jane')
    guardian.first_name = 'Janet'
    guardian.save_guardian()

    updated_guardian = Guardian.objects.all_with_deleted().get(phone_number='0987654321')
    self.assertEqual(updated_guardian.first_name, 'Janet')
