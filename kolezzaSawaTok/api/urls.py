from django.urls import path
from .views import SessionListView

'''Maps the URL path 'sessions/' to the SessionListView view.
This path is used for listing all sessions (GET) or creating a new session (POST).
The view is named 'session_list_view' for URL reversal purposes.
'''

'''Maps the URL path 'sessions/<int:session_id>/' to the SessionListView view.
This path is used for retrieving (GET), updating, or deleting a specific session
identified by the session_id. The session_id is captured from the URL and passed to the view.
The view is named 'session-detail' for URL reversal purposes.'''
urlpatterns = [
    path(
        "sessions/",
        SessionListView.as_view(),
        name="session_list_view"
    ),
    path(
        'sessions/<int:session_id>/',
        SessionListView.as_view(),
        name='session-detail'
    ),
]