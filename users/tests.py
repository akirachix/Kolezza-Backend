from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserManagerTest(TestCase):
    def setUp(self):
        self.email = "user@example.com"
        self.username = "testuser"
        self.password = "password123"

    def test_create_user_success(self):
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password,
        )
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)

    def test_create_user_without_email(self):
        # This will raise ValueError because email is required
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(
                email="",  # Provide an empty email string to simulate missing email
                username=self.username,
                password=self.password,
            )
        self.assertEqual(str(context.exception), "The Email field must be set")

    def test_create_superuser_success(self):
        superuser = User.objects.create_superuser(
            email=self.email, 
            username=self.username, 
            password=self.password
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_superuser_role(self):
        superuser = User.objects.create_superuser(
            email=self.email, 
            username=self.username, 
            password=self.password
        )
        self.assertEqual(superuser.role, "superadmin")

class UserModelTest(TestCase):
    def setUp(self):
        self.email = "user@example.com"
        self.username = "testuser"
        self.password = "password123"

    def test_user_role_speech_therapist(self):
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password,
            role="speech_therapist"
        )
        self.assertTrue(user.is_speech_therapist)
        self.assertFalse(user.is_superuser)

    def test_user_role_superadmin(self):
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password,
            role="superadmin"
        )
        self.assertTrue(user.is_superuser)
        self.assertFalse(user.is_speech_therapist)

    def test_user_default_role(self):
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password,
            role="other_role"
        )
        self.assertFalse(user.is_speech_therapist)

    def test_user_string_representation(self):
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password
        )
        self.assertEqual(str(user), user.username)
