from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    queryset = Note.objects.all().order_by('-created_at')