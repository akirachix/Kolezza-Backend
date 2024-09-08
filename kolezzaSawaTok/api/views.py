import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from session.models import Session
from .serializers import SessionSerializer

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
