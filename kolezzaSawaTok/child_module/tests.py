from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import ChildModule, LevelOfStuttering
from datetime import timedelta

class ChildModuleModelTest(TestCase):

    def setUp(self):
        # Happy path: Create a valid LevelOfStuttering instance
        self.level_of_stuttering = LevelOfStuttering.objects.create(
            type_of_stuttering='Developmental',
            description='Mild stuttering',
            duration=timedelta(days=30)  # Example duration
        )
        
        # Happy path: Create a valid ChildModule instance
        self.child_module = ChildModule.objects.create(
            name='Test Module',
            description='A module for testing',
            duration=timedelta(hours=1, minutes=30),  # Example duration of 1 hour 30 minutes
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering  # Link to LevelOfStuttering
        )
    
    # Happy path: Test ChildModule creation
    def test_child_module_creation(self):
        self.assertEqual(self.child_module.name, 'Test Module')
        self.assertEqual(self.child_module.description, 'A module for testing')
        self.assertEqual(self.child_module.duration, timedelta(hours=1, minutes=30))
        self.assertEqual(self.child_module.module_level, 1)
        self.assertEqual(self.child_module.level_of_stuttering_id, self.level_of_stuttering)

    # Happy path: Test __str__ method
    def test_child_module_str(self):
        self.assertEqual(str(self.child_module), '1')  # Test __str__ method returns module_level

    # Happy path: Test name max length (valid case)
    def test_child_module_name_max_length_valid(self):
        valid_name = 'A' * 50  # Exactly max_length=50
        child_module = ChildModule(
            name=valid_name,
            description='Description',
            duration=timedelta(hours=1),
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering
        )
        
        # Manually validate the model (no exception should be raised)
        try:
            child_module.full_clean()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")

    # Unhappy path: Test name max length exceeds limit
    def test_child_module_name_max_length_invalid(self):
        long_name = 'A' * 51  # More than max_length=50
        child_module = ChildModule(
            name=long_name,
            description='Description',
            duration=timedelta(hours=1),
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering
        )
        
        # Validate the model and expect a ValidationError
        with self.assertRaises(ValidationError):
            child_module.full_clean()  # This should raise ValidationError for name length

    # Unhappy path: Test description max length exceeds limit
    def test_child_module_description_max_length_invalid(self):
        long_description = 'B' * 51  # More than max_length=50
        child_module = ChildModule(
            name='Valid Name',
            description=long_description,
            duration=timedelta(hours=1),
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering
        )
        
        # Validate the model and expect a ValidationError
        with self.assertRaises(ValidationError):
            child_module.full_clean()  # This should raise ValidationError for description length

    # Unhappy path: Test missing required fields (e.g., duration)
    def test_child_module_missing_duration(self):
        child_module = ChildModule(
            name='Test Module',
            description='A module without duration',
            module_level=1,
            level_of_stuttering_id=self.level_of_stuttering
        )
        
        # Expect a ValidationError because duration is missing (None)
        with self.assertRaises(ValidationError):
            child_module.full_clean()  # This should raise ValidationError for missing duration

    # Unhappy path: Test invalid foreign key relationship
    def test_child_module_invalid_fk(self):
        child_module = ChildModule(
            name='Test Module',
            description='Invalid FK',
            duration=timedelta(hours=1),
            module_level=1,
            level_of_stuttering_id=None  # Invalid ForeignKey (None)
        )
        
        # Validate the model and expect a ValidationError for the ForeignKey
        with self.assertRaises(ValidationError):
            child_module.full_clean()  # This should raise ValidationError for missing FK
