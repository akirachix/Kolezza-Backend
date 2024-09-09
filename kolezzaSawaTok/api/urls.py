from django.urls import path
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
    path('levels-of-stuttering/', LevelOfStutteringListCreateView.as_view(), name='levels-of-stuttering-list-create'),
    path('levels-of-stuttering/<int:id>/', LevelOfStutteringDetailView.as_view(), name='levels-of-stuttering-detail'),
    path('guardians/', GuardianListCreateView.as_view(), name='guardians-list-create'),
    path('guardians/all/', GuardianListAllView.as_view(), name='guardians-list-all'), 
    path('guardian/<int:id>/', GuardianDetailView.as_view(), name='guardian-detail'),
     # Route for listing all child modules; mapped to the ChildModuleListView
    path('child_modules/', ChildModuleListView.as_view(), name='child_module_list_view'),
    
    # Route for retrieving, updating, or deleting a specific child module by ID; mapped to the ChildModuleDetailView
    path('child_module/<int:id>/', ChildModuleDetailView.as_view(), name='child_module_detail_view'),
]

