from django.urls import path
from .views import ChildProgressListView, ChildProgressDetailView
urlpatterns = [
    # For listing and creating child progress records
    path('api/child-progress/', ChildProgressListView.as_view(), name='child_progress_list'),
    # For retrieving, updating, and deleting a specific child progress record
    path('api/child-progress/<int:pk>/', ChildProgressDetailView.as_view(), name='child_progress_detail'),
]