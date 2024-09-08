
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from users.models import User
from .serializers import UserSerializer
from users.permissions import IsAuthenticatedAndHasPermission
from users.permissions import IsAuthenticatedAndHasPermission


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

