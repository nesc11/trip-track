from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('', views.api_root),
    path('trips/', views.TripList.as_view(), name='trip-list'),
    path('trips/<int:pk>/', views.TripDetail.as_view(), name='trip-detail'),
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
