from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from session.models import Session
from .serializers import SessionSerializer
from django.shortcuts import render
import logging
from child_progress.models import ChildProgress
from .serializers import ChildProgressSerializer
from django.core.exceptions import ValidationError
from rest_framework import serializers
from child_management.models import Child_Management
from speech_therapist.models import Speech_Therapist
from .serializers import SpeechTherapistSerializer, ChildManagementSerializer
from child_module.models import ChildModule
from .serializers import ChildModuleSerializer
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering
from .serializers import LevelOfStutteringSerializer, GuardianSerializer, UserSerializer
from django.contrib.auth import authenticate, login as django_login
from users.models import User
from rest_framework.permissions import AllowAny
from users.permissions import IsAuthenticatedAndHasPermission
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from rest_framework import generics


logger = logging.getLogger('session')
class SessionListView(APIView):
    '''View for listing all sessions, retrieving a specific session and creating a new session.'''


logger = logging.getLogger('session')

class SessionListView(APIView):
    '''View for listing all sessions, retrieving a specific session and creating a new session.'''
    def get(self, request, session_id=None):
        '''Handles GET requests to retrieve a specific session by ID or all sessions'''
        logger.debug("GET request is being processed with session_id: %s", session_id)
        if session_id:
            try:
                session = Session.objects.get(pk=session_id)
                serializer = SessionSerializer(session)
                logger.info("Session retrieved successfully: %s", session_id)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Session.DoesNotExist:
                logger.error("Session with id %s not found", session_id)
                return Response({"detail": "Unfortunately, the session does not exist in the system."}, status=status.HTTP_404_NOT_FOUND)
        else:
            sessions = Session.objects.all()
            serializer = SessionSerializer(sessions, many=True)
            logger.info("All sessions retrieved successfully")
            return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        '''Handles POST requests to create a new session,
        and saves data with a 201 status code or returns errors with a 400 status code.'''
        logger.debug("POST request received with data: %s", request.data)
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("New session has been created successfully: %s", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning("Failed to create this sessionbecause of validation errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Set up logging
logger = logging.getLogger(__name__)
"""List and create child progress records
GET method to list all child progress records
POST method to create a new child progress record
Validate and save child progress, ensuring no duplicates
for the same module and stuttering level
"""


class ChildProgressListView(APIView):
    def get(self, request):
        logger.info("Fetching all child progress records")
        progress = ChildProgress.objects.all()
        serializer = ChildProgressSerializer(progress, many=True)
        logger.info(f"Fetched {len(progress)} records")
        return Response(serializer.data)

    def post(self, request):
        logger.info("Creating new child progress record")
        serializer = ChildProgressSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                logger.info("Child progress record created successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                logger.error(f"Validation error: {e}")
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error(f"Creation failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Retrieve a specific child progress record by ID
Helper method to get a child progress object by its primary key (ID)
GET method to retrieve child progress by ID"""


class ChildProgressDetailView(APIView):
    def get_object(self, pk):
        try:
            return ChildProgress.objects.get(pk=pk)
        except ChildProgress.DoesNotExist:
            logger.error(f"Child progress with ID {pk} not found")
            return None

    def get(self, request, pk):
        logger.info(f"Fetching child progress record with ID {pk}")
        progress = self.get_object(pk)
        if progress is None:
            logger.error(f"No child progress record found with ID {pk}")
            return Response(
                {"error": "Child progress record not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ChildProgressSerializer(progress)
        logger.info(f"Fetched child progress record for ID {pk}")
        return Response(serializer.data)


"""Create a logger instance to log events in this file"""
logger = logging.getLogger(__name__)

"""View to list all speech therapists"""
"""Fetch all speech therapists"""
class SpeechTherapistListView(generics.ListAPIView):
    """
    View to list all Speech Therapists.
    """
    queryset = Speech_Therapist.objects.all()
    serializer_class = SpeechTherapistSerializer
  
"""Get a single therapist by ID"""
class SpeechTherapistDetailView(APIView):
   def get(self, request, id):
       logger.info("Fetching speech therapist with ID: %s", id)
       try:
           speech_therapists = Speech_Therapist.objects.get(id=id) 
           serializer = SpeechTherapistSerializer(speech_therapists) 
           logger.debug("Fetched therapist data: %s", serializer.data) 
           return Response(serializer.data, status=status.HTTP_200_OK) 
       except Speech_Therapist.DoesNotExist:
           logger.warning("Therapist with ID %s not found.", id) 
           return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)
       except Exception as e:
           logger.error("Error occurred while fetching therapist: %s", e) 
           return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   """Update a therapist's details"""
   def patch(self, request, id):
       logger.info("Updating speech therapist with ID: %s", id)
       try:
           speech_therapists = Speech_Therapist.objects.get(id=id)
           serializer = SpeechTherapistSerializer(speech_therapists, data=request.data, partial=True) 
           if serializer.is_valid():
               serializer.save() 
               logger.debug("Updated therapist data: %s", serializer.data)
               return Response(serializer.data)
           logger.warning("Validation errors: %s", serializer.errors) 
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Speech_Therapist.DoesNotExist:
           logger.warning("Therapist with ID %s not found for update.", id) 
           return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)


   """Soft delete a therapist"""
   def delete(self, request, id):
      
       logger.info("Deleting speech therapist with ID: %s", id) 
       try:
           speech_therapist = Speech_Therapist.objects.get(id=id, is_deleted=False) 
           speech_therapist.soft_delete() 
           logger.info("Therapist with ID %s deleted successfully.", id) 
           return Response({'message': 'Therapist deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
       except Speech_Therapist.DoesNotExist:
           logger.warning("Therapist with ID %s not found for deletion.", id) 
           return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)


  
"""Register a new therapist"""
class SpeechTherapistCreateView(generics.CreateAPIView):
    """
    View to create a new Speech Therapist.
    """
    queryset = Speech_Therapist.objects.all()
    serializer_class = SpeechTherapistSerializer


"""Fetch all children"""
class ChildManagementListView(APIView):
   def get(self, request):
       logger.info("Fetching all children.")
       child = Child_Management.objects.all() 
       serializer = ChildManagementSerializer(child, many=True) 
       logger.debug("Fetched children data: %s", serializer.data) 
       return Response({'child': serializer.data})


"""Register a new child"""
class RegisterChildView(APIView):
   def post(self, request):
       logger.info("Registering new child.") 
       serializer = ChildManagementSerializer(data=request.data) 
       if serializer.is_valid():
           serializer.save() 
           logger.info("Child registered successfully: %s", serializer.data) 
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       logger.warning("Validation errors during child registration: %s", serializer.errors) 
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Fetch, update, delete, and restore a specific child
Fetch a child by ID"""
class ChildManagementDetailView(APIView):
 
   def get(self, request, id):
       logger.info("Fetching child with ID: %s", id) 
       try:
           child = Child_Management.objects.get(id=id, is_deleted=False) 
           serializer = ChildManagementSerializer(child) 
           logger.debug("Fetched child data: %s", serializer.data) 
           return Response(serializer.data, status=status.HTTP_200_OK)
       except Child_Management.DoesNotExist:
           logger.warning("Child with ID %s not found.", id) 
           return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)
       except Exception as e:
           logger.error("Error occurred while fetching child: %s", e) 
           return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
   def patch(self, request, id):
       logger.info("Updating speech therapist with ID: %s", id)
       try:
           speech_therapists = Child_Management.objects.get(id=id)
           serializer = ChildManagementSerializer(speech_therapists, data=request.data, partial=True) 
           if serializer.is_valid():
               serializer.save() 
               logger.debug("Updated therapist data: %s", serializer.data)
               return Response(serializer.data)
           logger.warning("Validation errors: %s", serializer.errors) 
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Child_Management.DoesNotExist:
           logger.warning("Therapist with ID %s not found for update.", id) 
           return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)




   """Soft delete a child"""
   def delete(self, request, id):
       logger.info("Deleting child with ID: %s", id) 
       try:
           child = Child_Management.objects.get(id=id, is_deleted=True) 
           child.soft_delete() 
           logger.info("Child with ID %s deleted successfully.", id) 
           return Response({'message': 'Child deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
       except Child_Management.DoesNotExist:
           logger.warning("Child with ID %s not found for deletion.", id) 
           return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)



# Initialize logger for logging messages
logger = logging.getLogger("child_module")  # Use the app name as the logger name


class ChildModuleListView(APIView):
    """
    Handles GET and POST requests for ChildModule instances.
    """

    def get(self, request):
        logger.info("GET request received for child modules.")
        """ Retrieves all ChildModule instances and returns them as a response. """
        try:
            logger.info("GET request received for child modules.")
            logger.info("Retrieving all ChildModule instances.")
            child_module = ChildModule.objects.all()
            serializer = ChildModuleSerializer(child_module, many=True)
            logger.info("Successfully retrieved ChildModule instances.")
            return Response(serializer.data)
        except Exception as e:
            logger.error(
                "An error occurred while retrieving ChildModule instances: %s", str(e)
            )
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        """Creates a new ChildModule instance and returns the created instance data."""
        logger.info("Creating a new ChildModule instance with data: %s", request.data)
        serializer = ChildModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(
                "Successfully created ChildModule instance: %s", serializer.data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning(
                "Failed to create ChildModule instance. Errors: %s", serializer.errors
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChildModuleDetailView(APIView):
    """
    Handles GET and PUT requests for a specific ChildModule instance.
    - GET: Retrieves a specific ChildModule instance by ID.
    - PUT: Updates an existing ChildModule instance.
    """

    def get(self, request, id):
        """Retrieves a specific ChildModule instance by ID."""
        try:
            logger.info("Retrieving ChildModule instance with ID: %s", id)
            child_module = ChildModule.objects.get(id=id)
            serializer = ChildModuleSerializer(child_module)
            logger.info(
                "Successfully retrieved ChildModule instance: %s", serializer.data
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ChildModule.DoesNotExist:
            logger.warning("ChildModule with ID %s does not exist.", id)
            return Response(
                {
                    "detail": "The application is unable to locate the specified ChildModule."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            logger.error(
                "An error occurred while retrieving ChildModule instance: %s", str(e)
            )
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, id):
        """Updates an existing ChildModule instance."""
        try:
            logger.info("Updating ChildModule instance with ID: %s", id)
            child_module = ChildModule.objects.get(id=id)
        except ChildModule.DoesNotExist:
            logger.warning("ChildModule with ID %s does not exist.", id)
            return Response(
                {
                    "detail": "The application is unable to locate the specified ChildModule."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ChildModuleSerializer(
            child_module, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            logger.info(
                "Successfully updated ChildModule instance: %s", serializer.data
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.warning(
                "Failed to update ChildModule instance. Errors: %s", serializer.errors
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LevelOfStutteringListCreateView(APIView):
    """
    List all Level of Stuttering records or create a new one.
    """

    def get(self, request):
        """
        Retrieve a list of all Level of Stuttering records.
        """
        try:
            levels = LevelOfStuttering.objects.all()
            serializer = LevelOfStutteringSerializer(levels, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving levels of stuttering: {e}")
            return Response(
                {"error": "Failed to retrieve levels."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        """
        Create a new Level of Stuttering record.
        """
        serializer = LevelOfStutteringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LevelOfStutteringDetailView(APIView):
    """
    Retrieve, update, or partially update a specific Level of Stuttering record.
    """

    def get_object(self, id):
        """
        Retrieve a Level of Stuttering record by its ID.
        """
        try:
            return LevelOfStuttering.objects.get(id=id)
        except LevelOfStuttering.DoesNotExist:
            logger.warning(f"Level of Stuttering with ID {id} does not exist.")
            return None

    def get(self, request, id):
        """
        Retrieve a specific Level of Stuttering record.
        """
        level = self.get_object(id)
        if level is None:
            return Response(
                {"error": "Level of Stuttering not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = LevelOfStutteringSerializer(level)
        return Response(serializer.data)

    def patch(self, request, id):
        """
        Partially update a specific Level of Stuttering record.
        """
        level = self.get_object(id)
        if level is None:
            return Response(
                {"error": "Level of Stuttering not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = LevelOfStutteringSerializer(level, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuardianListCreateView(APIView):
    """
    List all active Guardians or create a new Guardian.
    """
    def get(self, request):
        """
        Retrieve a list of all active Guardians.
        """
        try:
            guardians = Guardian.objects.all()  
            serializer = GuardianSerializer(guardians, many=True)  
            return Response(serializer.data)  
        except Exception as e:
            logger.error(f"Error retrieving guardians: {e}") 
            return Response({"error": "Failed to retrieve guardians."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Create a new Guardian.
        """
        serializer = GuardianSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class GuardianListAllView(APIView):
    """
    List all Guardians, including those that are soft-deleted.
    """
    def get(self, request):
        """
        Retrieve a list of all Guardians, including soft-deleted ones.
        """
        try:
            guardians = Guardian.objects.all_with_deleted()  
            serializer = GuardianSerializer(guardians, many=True)  
            return Response(serializer.data) 
        except Exception as e:
            logger.error(f"Error retrieving all guardians: {e}")  
            return Response({"error": "Failed to retrieve all guardians."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GuardianDetailView(APIView):
    """
    Retrieve, update, or partially update a specific Guardian record.
    """
    def get_object(self, id):
        """
        Retrieve a Guardian record by its ID, including soft-deleted ones.
        """
        try:
            return Guardian.objects.all_with_deleted().get(id=id)  # Fetch even soft-deleted users
        except Guardian.DoesNotExist:
            logger.warning(f"Guardian with ID {id} does not exist.")
            return None


    def get(self, request, id):
        """
        Retrieve a specific Guardian record.
        """
        guardian = self.get_object(id)  
        if guardian is None:
            return Response({"error": "Guardian not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = GuardianSerializer(guardian)  
        return Response(serializer.data)  
    
    def put(self, request, id):
        """
        Completely update a specific Guardian record.
        """
        guardian = self.get_object(id) 
        if guardian is None:
            return Response({"error": "Guardian not found."}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = GuardianSerializer(guardian, data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        """
        Partially update a specific Guardian record.
        """
        guardian = self.get_object(id)  
        if guardian is None:
            return Response({"error": "Guardian not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request is trying to restore a soft-deleted guardian
        if 'is_active' in request.data and request.data['is_active'] and not guardian.is_active:
            guardian.is_active = True
            guardian.save_guardian()  
            return Response({"message": "Guardian restored successfully."}, status=status.HTTP_200_OK)

        # Proceed with other updates
        serializer = GuardianSerializer(guardian, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)  

        logger.error(f"Validation errors: {serializer.errors}")  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        """
        Soft delete a specific Guardian record.
        """
        guardian = self.get_object(id)  
        if guardian is None:
            return Response({"error": "Guardian not found."}, status=status.HTTP_404_NOT_FOUND)
        guardian.soft_delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)


# UserListView Class:
# Handles listing all users and returns them as a JSON response.
class UserListView(APIView):
    # Method to handle GET requests and list all users
    def get(self, request):
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


# UserDetailView Class:
# Handles operations for a specific user identified by ID.
class CurrentUserView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request):
        user = request.user  
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserDetailView(APIView):

    # GET Method: Retrieves a specific user by ID, returns user data or errors.
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # PATCH Method: Partially updates a specific user by ID, saves updates or returns validation errors.
    def patch(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

    # DELETE Method: Deletes a specific user by ID and returns a success response or error if user not found.
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )


class RegisterView(APIView):
    # Method to handle POST requests for user registration
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the new user
            # Generate JWT tokens but do not include them in the response
            refresh = RefreshToken.for_user(user)
            # Return success message without token in response
            response = Response({
                'message': 'Registration successful',
            }, status=status.HTTP_201_CREATED)
            # Set the access token in an HTTP-only cookie
            response.set_cookie(
                key='access_token',  # Adjust the cookie name if needed
                value=str(refresh.access_token),
                httponly=True,  # Prevent client-side access
                secure=True,  # Ensure it's sent over HTTPS (use False in development)
                samesite='Lax',  # Adjust SameSite attribute based on your requirements
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YourProtectedView(APIView):
    permission_classes = [IsAuthenticatedAndHasPermission]

    def get(self, request, *args, **kwargs):
        # Your view logic here
        return Response({"message": "You have access to this view!"})
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            response = Response({
                'message': 'Login successful',
                'access_token': str(refresh.access_token),  # Return access token
                'refresh_token': str(refresh), 
                'userId':user.id,
                'role': user.role 
            }, status=status.HTTP_200_OK)
            
            # Optionally set the token in the cookie
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=str(refresh.access_token),
                httponly=True,
                secure=False,  # Set to True for production
                samesite='Lax',
            )
            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

class CreateAdminUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")
        first_name = request.data.get("firstname")
        last_name = request.data.get("lastname")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            return Response(
                {"detail": "Superuser created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"detail": "Superuser already exists"}, status=status.HTTP_400_BAD_REQUEST
        )
