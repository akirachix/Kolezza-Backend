# api/views.py
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from child_module.models import ChildModule
from .serializers import ChildModuleSerializer

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