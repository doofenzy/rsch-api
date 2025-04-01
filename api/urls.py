from django.urls import path
from . import views
    

urlpatterns = [
    path("research/", views.CreateResearchView.as_view(), name="create-research"),
    path("research/delete<int:pk>", views.DeleteResearchView.as_view(), name="delete-research"),
]
