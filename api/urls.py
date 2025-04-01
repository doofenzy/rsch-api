from django.urls import path
from . import views
    

urlpatterns = [
    path("research/", views.CreateResearchView.as_view(), name="create-research"),
    path("research/all/", views.ListResearch.as_view(), name="list-research-all"),
    path("research/delete<int:pk>", views.DeleteResearchView.as_view(), name="delete-research"),
]
