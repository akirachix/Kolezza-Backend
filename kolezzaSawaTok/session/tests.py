from django.test import TestCase
from django.db import IntegrityError
from datetime import date, time, timedelta
from .models import Session
from level_of_stuttering.models import LevelOfStuttering
from child_progress.models import ChildProgress

class SessionModelTest(TestCase):

    def setUp(self):
        '''Create a session instance and a child_progress instance for testing'''
        
        # Create a LevelOfStuttering instance
        self.level_of_stuttering = LevelOfStuttering.objects.create(
            description="Moderate stuttering with some difficulty speaking."
        )
        
        # Create a ChildProgress instance with all required fields
        self.child_progress = ChildProgress.objects.create(
            started_module_at=date(2024, 9, 1),  # Provide a valid date
            finished_module_at=date(2024, 12, 1),  # Provide a valid date
            current_level_of_stuttering_id= self.level_of_stuttering
        )

        # Create a Session instance
        self.session = Session.objects.create(
            child_progress=self.child_progress,  # Assign the child_progress instance
            session_date=date(2024, 9, 5),
            session_start_time=time(9, 0),
            session_end_time=time(10, 30)
        )

    def test_duration_calculation_success(self):
        '''Test if the duration calculation is correct'''
        expected_duration = timedelta(hours=1, minutes=30)
        saved_session = Session.objects.get(id=self.session.id)
        self.assertEqual(saved_session.duration, expected_duration)

    def test_duration_calculation_no_duration(self):
        '''Test if duration is zero when end time is before start time'''
        invalid_session = Session.objects.create(
            child_progress=self.child_progress,  # Assign the child_progress instance
            session_date=date(2024, 9, 5),
            session_start_time=time(10, 30),
            session_end_time=time(9, 0)
        )
        saved_session = Session.objects.get(id=invalid_session.id)
        self.assertEqual(saved_session.duration, timedelta(seconds=81000))

    def test_duration_calculation_missing_start_time(self):
        '''Test if IntegrityError is raised when start time is missing'''
        incomplete_session = Session(
            child_progress=self.child_progress,  # Assign the child_progress instance
            session_date=date(2024, 9, 5),
            session_end_time=time(10, 30)  # Omitting the start time
        )
        with self.assertRaises(IntegrityError):
            incomplete_session.save()

    def test_duration_calculation_missing_end_time(self):
        '''Test if IntegrityError is raised when end time is missing'''
        incomplete_session = Session(
            child_progress=self.child_progress,  # Assign the child_progress instance
            session_date=date(2024, 9, 5),
            session_start_time=time(9, 0)  # Omitting the end time
        )
        with self.assertRaises(IntegrityError):
            incomplete_session.save()

