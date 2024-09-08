from django.urls import path
from .views import (
    GuardianListAllView,
    LevelOfStutteringListCreateView,
    LevelOfStutteringDetailView,
    GuardianListCreateView,
    GuardianDetailView,
)

urlpatterns = [
    path('levels-of-stuttering/', LevelOfStutteringListCreateView.as_view(), name='levels-of-stuttering-list-create'),
    path('levels-of-stuttering/<int:id>/', LevelOfStutteringDetailView.as_view(), name='levels-of-stuttering-detail'),
    path('guardians/', GuardianListCreateView.as_view(), name='guardians-list-create'),
    path('guardians/all/', GuardianListAllView.as_view(), name='guardians-list-all'), 
    path('guardian/<int:id>/', GuardianDetailView.as_view(), name='guardian-detail'),
]
