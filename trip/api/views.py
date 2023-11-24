from rest_framework import generics, permissions

from trip.models import Trip, Note, User
from .serializers import TripSerializer, NoteSerializer, UserSerializer
from .permissions import IsTripOwnerOrReadOnly, IsNoteOwnerOrReadOnly


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:user-list', request=request, format=format),
        'trips': reverse('api:trip-list', request=request, format=format),
        'notes': reverse('api:note-list', request=request, format=format)
    })


class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTripOwnerOrReadOnly]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class NoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsNoteOwnerOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Read-only views for the user representations
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
