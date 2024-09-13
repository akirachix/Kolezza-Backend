from django.urls import path
from .views import SessionListView
from .views import ChildProgressListView, ChildProgressDetailView
from .views import SpeechTherapistDetailView, ChildManagementDetailView
from .views import SpeechTherapistListView, ChildManagementListView
from .views import RegisterChildView, RegisterTherapistView
from .views import ChildModuleListView
from .views import ChildModuleDetailView
from .views import UserListView, UserDetailView, RegisterView, LoginView
from .views import CreateAdminUser
from .views import (
    GuardianListAllView,
    LevelOfStutteringListCreateView,
    LevelOfStutteringDetailView,
    GuardianListCreateView,
    GuardianDetailView,
)
from .views import SessionListView
'''Maps the URL path 'sessions/' to the SessionListView view.
This path is used for listing all sessions (GET) or creating a new session (POST).
The view is named 'session_list_view' for URL reversal purposes.
'''
'''Maps the URL path 'sessions/<int:session_id>/' to the SessionListView view.
This path is used for retrieving (GET), updating, or deleting a specific session
identified by the session_id. The session_id is captured from the URL and passed to the view.
The view is named 'session-detail' for URL reversal purposes.'''


'''Maps the URL path 'sessions/' to the SessionListView view.
This path is used for listing all sessions (GET) or creating a new session (POST).
The view is named 'session_list_view' for URL reversal purposes.
'''

'''Maps the URL path 'sessions/<int:session_id>/' to the SessionListView view.
This path is used for retrieving (GET), updating, or deleting a specific session
identified by the session_id. The session_id is captured from the URL and passed to the view.
The view is named 'session-detail' for URL reversal purposes.'''

# URL patterns for user-related views
urlpatterns = [
    # URL pattern for retrieving, updating, or deleting a specific user by ID
    path("user/<int:id>/", UserDetailView.as_view(), name="user_detail_view"),
    # URL pattern for listing all users
    path("users/", UserListView.as_view(), name="user_view"),
    # URL pattern for user registration
    path("register/", RegisterView.as_view(), name="register_view"),
    # URL pattern for login
    path("login/", LoginView.as_view(), name="login_view"),
    path("create-admin/", CreateAdminUser.as_view(), name="create_admin"),
    path(
        "levels-of-stuttering/",
        LevelOfStutteringListCreateView.as_view(),
        name="levels-of-stuttering-list-create",
    ),
    path(
        "levels-of-stuttering/<int:id>/",
        LevelOfStutteringDetailView.as_view(),
        name="levels-of-stuttering-detail",
    ),
    path("guardians/", GuardianListCreateView.as_view(), name="guardians-list-create"),
    path("guardians/all/", GuardianListAllView.as_view(), name="guardians-list-all"),
    path("guardian/<int:id>/", GuardianDetailView.as_view(), name="guardian-detail"),
    # Route for listing all child modules; mapped to the ChildModuleListView
    path(
        "child_modules/", ChildModuleListView.as_view(), name="child_module_list_view"
    ),
    # Route for retrieving, updating, or deleting a specific child module by ID; mapped to the ChildModuleDetailView
    path(
        "child_module/<int:id>/",
        ChildModuleDetailView.as_view(),
        name="child_module_detail_view",
    ),
    path(
        "therapist/<int:id>/",
        SpeechTherapistDetailView.as_view(),
        name="therapist_detail_view",
    ),
    path("therapists/", SpeechTherapistListView.as_view(), name="therapist_view"),
    path(
        "therapist_registration/",
        RegisterTherapistView.as_view(),
        name="register_therapist_view",
    ),
    path(
        "therapist/<int:id>/restore/",
        SpeechTherapistDetailView.as_view(),
        name="therapist_restore_view",
    ),
    path(
        "child/<int:id>/", ChildManagementDetailView.as_view(), name="child_detail_view"
    ),
    path("children/", ChildManagementListView.as_view(), name="child_view"),
    path(
        "child_registration/", RegisterChildView.as_view(), name="register_child_view"
    ),
    path(
        "child/<int:id>/restore/",
        ChildManagementDetailView.as_view(),
        name="child_restore_view",
    ),
    # For listing and creating child progress records
    path(
        "api/child-progress/",
        ChildProgressListView.as_view(),
        name="child_progress_list",
    ),
    # For retrieving, updating, and deleting a specific child progress record
    path(
        "api/child-progress/<int:pk>/",
        ChildProgressDetailView.as_view(),
        name="child_progress_detail",
    ),
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