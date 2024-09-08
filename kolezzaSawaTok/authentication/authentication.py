from django.contrib.auth.models import User



class Auth0Backend:
    """
    Custom authentication backend for handling Auth0 user authentication.
    """
    
    def authenticate(self, request, user_info=None):
        """
        Authenticate a user based on the provided user_info from Auth0.

        Args:
            request: The HTTP request object.
            user_info (dict): Information about the user obtained from Auth0. Expected to contain 'email'.

        Returns:
            User: The authenticated user instance, or None if authentication fails.
        """
        if user_info:
            # Attempt to get or create a user with the provided email address
            user, created = User.objects.get_or_create(username=user_info['email'])
            
            if created:
                # If the user was newly created, set their email address
                user.email = user_info['email']
                user.save()
            
            # Return the user instance
            return user
        
        # Return None if user_info is not provided or authentication fails
        return None
