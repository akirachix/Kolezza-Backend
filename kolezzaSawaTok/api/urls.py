from django.urls import path
from .views import SpeechTherapistDetailView, ChildManagementDetailView
from .views import SpeechTherapistListView, ChildManagementListView
from .views import RegisterChildView, RegisterTherapistView



urlpatterns=[
    path(
        'therapist/<int:id>/', SpeechTherapistDetailView.as_view(),name="therapist_detail_view"),
    path(
        'therapists/', SpeechTherapistListView.as_view(), name="therapist_view"),

    path(
       'therapist_registration/', RegisterTherapistView.as_view(), name="register_therapist_view" 
    ), 
    path(
        'therapist/<int:id>/restore/', SpeechTherapistDetailView.as_view(), name="therapist_restore_view"
        ),
    path(
        'child/<int:id>/', ChildManagementDetailView.as_view(),name="child_detail_view"),
    path(
        'children/', ChildManagementListView.as_view(), name="child_view"),

    path(
        'child_registration/', RegisterChildView.as_view(), name="register_child_view" 
    ),        
        
    path(
        'child/<int:id>/restore/', ChildManagementDetailView.as_view(), name="child_restore_view"
        ),


]