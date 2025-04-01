from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import UserSerializer, AuthorsSerializer, ResearchSerializer, ReviewsSerializer
from .models import Research, Authors, Reviews
# Create your views here.

class CreateResearchView(generics.ListCreateAPIView):
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Research.objects.filter(authors__user=user)


    def perform_create(self, serializer):
        research = serializer.save()
        Authors.objects.create(research=research, user=self.request.user)


class ListResearch(generics.ListAPIView):
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Research.objects.all()


class DeleteResearchView(generics.DestroyAPIView):
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Research.objects.filter(authors__user=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



