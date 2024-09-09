from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView
from .views import CreateAdminUser


# URL patterns for user-related views
urlpatterns = [
    # URL pattern for retrieving, updating, or deleting a specific user by ID
    path(
        'user/<int:id>/',  
        UserDetailView.as_view(), 
        name="user_detail_view"  
    ),
    
    # URL pattern for listing all users
    path(
        'users/', 
        UserListView.as_view(),  
        name="user_view"  
    ),
    
    # URL pattern for user registration
    path(
        'register/',  
        RegisterView.as_view(),  
        name="register_view"  
    ),

    
    # URL pattern for login
    path(
        'login/',
        LoginView.as_view(),
        name='login_view'
    ),
    
    path(
        'create-admin/', 
        CreateAdminUser.as_view(), 
        name='create_admin'
    ),
]
