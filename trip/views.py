from typing import Any
from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Trip, Note

# Home


class HomeView(TemplateView):
    template_name = 'trip/index.html'


# Trip views

class TripListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Remember to check only aut user acces their trips
class TripDetailView(LoginRequiredMixin, DetailView):
    # Limit the list of objects where the view is going to search
    # queryset = Trip.objects.filter(pk__gt=4)  ----> model=Trip   ---same---   queryset = Trip.objects.all()

    def get_object(self, queryset=None):
        return get_object_or_404(Trip, pk=self.kwargs.get('pk'), owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context


class TripUpdateView(LoginRequiredMixin, UpdateView):
    # model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def get_object(self, queryset=None):
        return get_object_or_404(Trip, pk=self.kwargs.get('pk'), owner=self.request.user)


class TripDeleteView(LoginRequiredMixin, DeleteView):
    # model = Trip
    success_url = reverse_lazy('trip-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Trip, pk=self.kwargs.get('pk'), owner=self.request.user)


# Note views

class NoteListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)


class NoteDetailView(LoginRequiredMixin, DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(Note, trip__owner=self.request.user, pk=self.kwargs.get('pk'))


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Note, trip__owner=self.request.user, pk=self.kwargs.get('pk'))

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    # model = Note
    success_url = reverse_lazy('note-list')
    # Note template needed - POST request sended

    def get_object(self, queryset=None):
        return get_object_or_404(Note, trip__owner=self.request.user, pk=self.kwargs.get('pk'))
