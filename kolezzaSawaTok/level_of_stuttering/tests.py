from django.test import TestCase
from datetime import timedelta
from level_of_stuttering.models import LevelOfStuttering

class LevelOfStutteringTestCase(TestCase):

    def setUp(self):
        # Create a LevelOfStuttering record with duration in hours, minutes, and seconds
        LevelOfStuttering.objects.create(
            type_of_stuttering="Developmental",
            description="Occurs in early childhood, often between the ages of 2 to 6.",
            duration=timedelta(hours=3, minutes=15, seconds=30)
        )

    def test_level_of_stuttering_creation(self):
        """Test that a LevelOfStuttering object is created correctly."""
        stuttering_record = LevelOfStuttering.objects.get(type_of_stuttering="Developmental")
        self.assertEqual(stuttering_record.description, "Occurs in early childhood, often between the ages of 2 to 6.")
        self.assertEqual(stuttering_record.duration, timedelta(hours=3, minutes=15, seconds=30))

    def test_str_method(self):
        """Test the __str__ method returns the type_of_stuttering as expected."""
        stuttering_record = LevelOfStuttering.objects.get(type_of_stuttering="Developmental")
        self.assertEqual(str(stuttering_record), "Developmental")
