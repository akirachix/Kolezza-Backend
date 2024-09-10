from django.urls import path
from . import views
# URL patterns for child progress API views
urlpatterns = [
    # URL for listing all child progress records and creating a new child progress record
    # GET: Fetches all child progress records
    # POST: Creates a new child progress record
    path('api/child-progress/', views.ChildProgressListView.as_view(), name='child_progress_list'),
    # URL for retrieving a specific child progress record by its primary key (ID)
    # GET: Fetches a single child progress record by ID
    path('api/child-progress/<int:pk>/', views.ChildProgressDetailView.as_view(), name='child_progress_detail'),
]












