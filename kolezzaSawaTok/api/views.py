from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering
from .serializers import LevelOfStutteringSerializer, GuardianSerializer
import logging

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
