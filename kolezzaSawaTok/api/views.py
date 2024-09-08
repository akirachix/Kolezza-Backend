from django.shortcuts import render
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from child_management.models import Child_Management
from speech_therapist.models import Speech_Therapist
from .serializers import SpeechTherapistSerializer, ChildManagementSerializer
from rest_framework import status

"""Create a logger instance to log events in this file"""
logger = logging.getLogger(__name__)

"""View to list all speech therapists"""
"""Fetch all speech therapists"""
class SpeechTherapistListView(APIView):
    def get(self, request):
      
        logger.info("Fetching all speech therapists.")
        speech_therapists = Speech_Therapist.objects.all()  
        serializer = SpeechTherapistSerializer(speech_therapists, many=True)  
        logger.debug("Fetched speech therapists: %s", serializer.data)  
        return Response({'speech therapists': serializer.data})  
    
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
            speech_therapist = Speech_Therapist.objects.get(id=id, is_updated=False)  
            speech_therapist.soft_delete()  
            logger.info("Therapist with ID %s deleted successfully.", id)  
            return Response({'message': 'Therapist deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Speech_Therapist.DoesNotExist:
            logger.warning("Therapist with ID %s not found for deletion.", id)  
            return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)

    """Restore a soft-deleted therapist"""
    def restore(self, request, id):
        logger.info("Restoring speech therapist with ID: %s", id)  
        try:
            speech_therapist = Speech_Therapist.objects.get(id=id, is_updated=True)  
            speech_therapist.restore()  
            logger.info("Therapist with ID %s restored successfully.", id)  
            return Response({'message': 'Therapist restored successfully'}, status=status.HTTP_200_OK)
        except Speech_Therapist.DoesNotExist:
            logger.warning("Therapist with ID %s not found for restoration.", id)  
            return Response({'error': 'Therapist not found'}, status=status.HTTP_404_NOT_FOUND)

"""Register a new therapist"""
class RegisterTherapistView(APIView):
    def post(self, request):
        logger.info("Registering new speech therapist.")  
        serializer = SpeechTherapistSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save() 
            logger.info("Therapist registered successfully: %s", serializer.data)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Validation errors during therapist registration: %s", serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            child = Child_Management.objects.get(id=id, is_updated=False)  
            serializer = ChildManagementSerializer(child)  
            logger.debug("Fetched child data: %s", serializer.data)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Child_Management.DoesNotExist:
            logger.warning("Child with ID %s not found.", id)  
            return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error("Error occurred while fetching child: %s", e)  
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    """Update a child’s details"""
    def patch(self, request, id):
        logger.info("Updating child with ID: %s", id)  
        try:
            child = Child_Management.objects.get(id=id, is_updated=False)  
            serializer = ChildManagementSerializer(child, data=request.data, partial=True)  
            if serializer.is_valid():
                serializer.save()  
                logger.debug("Updated child data: %s", serializer.data)  
                return Response(serializer.data)
            logger.warning("Validation errors during child update: %s", serializer.errors)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Child_Management.DoesNotExist:
            logger.warning("Child with ID %s not found for update.", id)  
            return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    """Soft delete a child"""
    def delete(self, request, id):
        logger.info("Deleting child with ID: %s", id)  
        try:
            child = Child_Management.objects.get(id=id, is_updated=False)  
            child.soft_delete()  
            logger.info("Child with ID %s deleted successfully.", id)  
            return Response({'message': 'Child deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Child_Management.DoesNotExist:
            logger.warning("Child with ID %s not found for deletion.", id)  
            return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    """Restore a soft-deleted child"""
    def restore(self, request, id):
        logger.info("Restoring child with ID: %s", id)  
        try:
            child = Child_Management.objects.get(id=id, is_updated=True)  
            child.restore()  
            logger.info("Child with ID %s restored successfully.", id)  
            return Response({'message': 'Child restored successfully'}, status=status.HTTP_200_OK)
        except Child_Management.DoesNotExist:
            logger.warning("Child with ID %s not found for restoration.", id)  
            return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)
