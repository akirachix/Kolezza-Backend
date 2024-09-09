
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from users.models import User
from .serializers import UserSerializer
from users.permissions import IsAuthenticatedAndHasPermission
from django.contrib.auth import authenticate, login as django_login
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated



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
        

# RegisterView Class:
# Handles user registration by accepting POST requests with user data, saving the new user,
# and returning the result or validation errors.
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
    




