from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import logging
from child_progress.models import ChildProgress
from .serializers import ChildProgressSerializer
from django.core.exceptions import ValidationError
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
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
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
            return Response({'error': 'Child progress record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ChildProgressSerializer(progress)
        logger.info(f"Fetched child progress record for ID {pk}")
        return Response(serializer.data)