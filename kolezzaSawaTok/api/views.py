# api/views.py
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from child_module.models import ChildModule
from .serializers import ChildModuleSerializer
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering
from .serializers import LevelOfStutteringSerializer, GuardianSerializer,UserSerializer
from django.contrib.auth import authenticate, login as django_login
from users.models import User
from rest_framework.permissions import AllowAny
from users.permissions import IsAuthenticatedAndHasPermission

# Initialize logger for logging messages
logger = logging.getLogger('child_module')  # Use the app name as the logger name

class ChildModuleListView(APIView):
    ''' 
    Handles GET and POST requests for ChildModule instances.
    '''
    def get(self, request):
        logger.info('GET request received for child modules.')
        ''' Retrieves all ChildModule instances and returns them as a response. '''
        try:
            logger.info('GET request received for child modules.')
            logger.info('Retrieving all ChildModule instances.')
            child_module = ChildModule.objects.all()
            serializer = ChildModuleSerializer(child_module, many=True)
            logger.info('Successfully retrieved ChildModule instances.')
            return Response(serializer.data)
        except Exception as e:
            logger.error('An error occurred while retrieving ChildModule instances: %s', str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        ''' Creates a new ChildModule instance and returns the created instance data. '''
        logger.info('Creating a new ChildModule instance with data: %s', request.data)
        serializer = ChildModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Successfully created ChildModule instance: %s', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning('Failed to create ChildModule instance. Errors: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChildModuleDetailView(APIView):
    ''' 
    Handles GET and PUT requests for a specific ChildModule instance.
    - GET: Retrieves a specific ChildModule instance by ID.
    - PUT: Updates an existing ChildModule instance.
    '''
    def get(self, request, id):
        ''' Retrieves a specific ChildModule instance by ID. '''
        try:
            logger.info('Retrieving ChildModule instance with ID: %s', id)
            child_module = ChildModule.objects.get(id=id)
            serializer = ChildModuleSerializer(child_module)
            logger.info('Successfully retrieved ChildModule instance: %s', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ChildModule.DoesNotExist:
            logger.warning('ChildModule with ID %s does not exist.', id)
            return Response({"detail": "The application is unable to locate the specified ChildModule."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error('An error occurred while retrieving ChildModule instance: %s', str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        ''' Updates an existing ChildModule instance. '''
        try:
            logger.info('Updating ChildModule instance with ID: %s', id)
            child_module = ChildModule.objects.get(id=id)
        except ChildModule.DoesNotExist:
            logger.warning('ChildModule with ID %s does not exist.', id)
            return Response({"detail": "The application is unable to locate the specified ChildModule."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChildModuleSerializer(child_module, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info('Successfully updated ChildModule instance: %s', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.warning('Failed to update ChildModule instance. Errors: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Set up logging for debugging and error tracking
logger = logging.getLogger(__name__)

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
            return Response({"error": "Failed to retrieve levels."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            return Response({"error": "Level of Stuttering not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LevelOfStutteringSerializer(level)  
        return Response(serializer.data)  

    def patch(self, request, id):
        """
        Partially update a specific Level of Stuttering record.
        """
        level = self.get_object(id)  
        if level is None:
            return Response({"error": "Level of Stuttering not found."}, status=status.HTTP_404_NOT_FOUND)
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
        logger.info("Request data: %s", request.data)
        try:
            serializer = GuardianSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning("Validation errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("An error occurred: %s", str(e))
            return Response({"error": "An internal error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        Retrieve a Guardian record by its ID.
        """
        try:
            return Guardian.objects.get(id=id)  
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

        serializer = GuardianSerializer(guardian, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data) 
        
        if 'is_active' in request.data and request.data['is_active']:
            guardian.is_active = True
            guardian.save_guardian()  
            return Response({"message": "Guardian restored successfully."}, status=status.HTTP_200_OK)

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
        return Response({'users': serializer.data})
    

# UserDetailView Class:
# Handles operations for a specific user identified by ID.
class UserDetailView(APIView):
    
    # GET Method: Retrieves a specific user by ID, returns user data or errors.
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

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
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

    # DELETE Method: Deletes a specific user by ID and returns a success response or error if user not found.
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class RegisterView(APIView):
    # Method to handle POST requests for user registration
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class YourProtectedView(APIView):
    permission_classes = [IsAuthenticatedAndHasPermission]

    def get(self, request, *args, **kwargs):
        # Your view logic here
        return Response({"message": "You have access to this view!"})



class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    


class CreateAdminUser(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')


        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            return Response({"detail": "Superuser created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Superuser already exists"}, status=status.HTTP_400_BAD_REQUEST)
    




