from rest_framework import serializers

from trip.models import Trip, Note, User


class TripSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='api:trip-detail')
    notes = serializers.HyperlinkedRelatedField(
        many=True, view_name='api:note-detail', read_only=True)

    class Meta:
        model = Trip
        fields = ['url', 'id', 'city', 'country', 'start_date',
                  'end_date', 'owner', 'notes']


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:note-detail')
    trip = serializers.HyperlinkedRelatedField(
        view_name='api:trip-detail', queryset=Trip.objects.all())

    class Meta:
        model = Note
        fields = ['url', 'id', 'trip', 'name',
                  'description', 'type', 'img', 'rating']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # trips = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Trip.objects.all())

    trips = serializers.HyperlinkedRelatedField(
        many=True, view_name='api:trip-detail', read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'trips']
