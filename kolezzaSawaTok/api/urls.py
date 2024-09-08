from django.urls import path
from .views import UserListView, UserDetailView, RegisterView,YourProtectedView

# URL patterns for user-related views
urlpatterns = [
    # URL pattern for retrieving, updating, or deleting a specific user by ID
    # Matches URLs like '/user/1/', where '1' is the user ID
    
# UserDetailView Path:
    # Handles URLs that include a specific user ID.
    # The view manages operations such as retrieving, updating, or deleting a user identified by the given ID.
    path(
        'user/<int:id>/',  
        UserDetailView.as_view(), 
        name="user_detail_view"  
    ),
    
# UserListView Path:
    # Handles URLs for listing all users.
    # The view provides a list of all users in the system.
    path(
        'users/', 
        UserListView.as_view(),  
        name="user_view"  
    ),
    
# RegisterView Path:
    # Handles URLs for user registration.
    # The view manages the process of registering new users.
    path(
        'register/',  
        RegisterView.as_view(),  
        name="register_view"  
    ),


    path(
        'authorization/',
        YourProtectedView.as_view(),
        name="protected_view"
    )
]
