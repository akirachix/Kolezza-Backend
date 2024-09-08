from django.urls import path
from .views import ChildModuleListView
from .views import ChildModuleDetailView

# URL patterns for the child_module app
urlpatterns = [
    # Route for listing all child modules; mapped to the ChildModuleListView
    path('child_modules/', ChildModuleListView.as_view(), name='child_module_list_view'),
    
    # Route for retrieving, updating, or deleting a specific child module by ID; mapped to the ChildModuleDetailView
    path('child_module/<int:id>/', ChildModuleDetailView.as_view(), name='child_module_detail_view'),
]