# from django.core.exceptions import ValidationError
# from django.test import TestCase
# from child_progress.models import ChildProgress
# from level_of_stuttering.models import LevelOfStuttering
# from datetime import date, timedelta
# from django.db import models


# class ChildProgressModelTest(TestCase):
#     def setUp(self):
#         """Set up the initial data for testing"""
#         self.level_of_stuttering = LevelOfStuttering.objects.create(
#             type_of_stuttering="Mild",
#             description="The child has a mild level of stuttering.",
#             duration=timedelta(days=30))
#         self.child_progress = ChildProgress.objects.create(
#             started_module_at=date(2024, 9, 1),
#             finished_module_at=date(2024, 9, 10),
#             current_level_of_stuttering_id=self.level_of_stuttering
#         )
    
#     # Happy Moments
#     def test_child_progress_creation(self):
#         """Test that the ChildProgress object is created correctly (happy moment)"""
#         self.assertIsInstance(self.child_progress, ChildProgress)
#         self.assertEqual(self.child_progress.started_module_at, date(2024, 9, 1))
#         self.assertEqual(self.child_progress.finished_module_at, date(2024, 9, 10))
#         self.assertEqual(self.child_progress.current_level_of_stuttering_id, self.level_of_stuttering)
    
#     def test_child_progress_str_method(self):
#         """Test the string representation of ChildProgress (happy moment)"""
#         expected_str = f"Progress for Module: {self.child_progress.started_module_at} - Stuttering Level: {self.child_progress.finished_module_at}"
#         self.assertEqual(str(self.child_progress), expected_str)

#     def test_child_progress_relationship(self):
#         """Test the relationship between ChildProgress and LevelOfStuttering (happy moment)"""
#         self.assertEqual(self.child_progress.current_level_of_stuttering_id.type_of_stuttering, "Mild")
#         self.assertEqual(self.child_progress.current_level_of_stuttering_id.description, "The child has a mild level of stuttering.")
    
#     def test_child_progress_without_started_date(self):
#         """Test that ChildProgress creation fails without a started_module_at date (unhappy moment)"""
#         with self.assertRaises(ValidationError):
#             child_progress = ChildProgress(
#                 started_module_at=None,
#                 finished_module_at=date(2024, 9, 10),
#                 current_level_of_stuttering_id=self.level_of_stuttering
#             )
#             child_progress.full_clean()

#     def test_child_progress_invalid_date_range(self):
#         """Test that ChildProgress creation fails if finished_module_at is before started_module_at (unhappy moment)"""
#         child_progress = ChildProgress(
#             started_module_at=date(2024, 9, 10),
#             finished_module_at=date(2024, 9, 1),
#             current_level_of_stuttering_id=self.level_of_stuttering
#         )
#         with self.assertRaises(ValidationError):
#             child_progress.full_clean()  #

#     def test_child_progress_with_invalid_stuttering_level(self):
#         """Test that ChildProgress creation fails with an invalid LevelOfStuttering (unhappy moment)"""
#         with self.assertRaises(ValidationError):
#             child_progress = ChildProgress(
#                 started_module_at=date(2024, 9, 1),
#                 finished_module_at=date(2024, 9, 10),
#                 current_level_of_stuttering_id=None
#             )
#             child_progress.full_clean()

from django.core.exceptions import ValidationError
from django.test import TestCase
from child_progress.models import ChildProgress
from level_of_stuttering.models import LevelOfStuttering
from datetime import date, timedelta

class ChildProgressModelTest(TestCase):
    def setUp(self):
        """Set up the initial data for testing"""
        self.level_of_stuttering = LevelOfStuttering.objects.create(
            type_of_stuttering="Mild",
            description="The child has a mild level of stuttering.",
            duration=timedelta(days=30)
        )
        self.child_progress = ChildProgress.objects.create(
            started_module_at=date(2024, 9, 1),
            finished_module_at=date(2024, 9, 10),
            current_level_of_stuttering_id=self.level_of_stuttering
        )
    
    # Happy Moments
    def test_child_progress_creation(self):
        """Test that the ChildProgress object is created correctly (happy moment)"""
        self.assertIsInstance(self.child_progress, ChildProgress)
        self.assertEqual(self.child_progress.started_module_at, date(2024, 9, 1))
        self.assertEqual(self.child_progress.finished_module_at, date(2024, 9, 10))
        self.assertEqual(self.child_progress.current_level_of_stuttering_id, self.level_of_stuttering)
    
    def test_child_progress_str_method(self):
        """Test the string representation of ChildProgress (happy moment)"""
        expected_str = f"Progress for Module: {self.child_progress.started_module_at} - Stuttering Level: {self.child_progress.finished_module_at}"
        self.assertEqual(str(self.child_progress), expected_str)

    def test_child_progress_relationship(self):
        """Test the relationship between ChildProgress and LevelOfStuttering (happy moment)"""
        self.assertEqual(self.child_progress.current_level_of_stuttering_id.type_of_stuttering, "Mild")
        self.assertEqual(self.child_progress.current_level_of_stuttering_id.description, "The child has a mild level of stuttering.")
    
    def test_child_progress_without_started_date(self):
        """Test that ChildProgress creation fails without a started_module_at date (unhappy moment)"""
        child_progress = ChildProgress(
            started_module_at=None,
            finished_module_at=date(2024, 9, 10),
            current_level_of_stuttering_id=self.level_of_stuttering
        )
        with self.assertRaises(ValidationError):
            child_progress.full_clean()

    def test_child_progress_invalid_date_range(self):
        """Test that ChildProgress creation fails if finished_module_at is before started_module_at (unhappy moment)"""
        child_progress = ChildProgress(
            started_module_at=date(2024, 9, 10),
            finished_module_at=date(2024, 9, 1),
            current_level_of_stuttering_id=self.level_of_stuttering
        )
        with self.assertRaises(ValidationError):
            child_progress.full_clean()

    def test_child_progress_with_invalid_stuttering_level(self):
        """Test that ChildProgress creation fails with an invalid LevelOfStuttering (unhappy moment)"""
        child_progress = ChildProgress(
            started_module_at=date(2024, 9, 1),
            finished_module_at=date(2024, 9, 10),
            current_level_of_stuttering_id=None
        )
        with self.assertRaises(ValidationError):
            child_progress.full_clean()