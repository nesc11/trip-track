from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='trips')

    class Meta:
        ordering = ['city']

    def __str__(self):
        return self.city


class Note(models.Model):

    EXCURSIONS = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General')
    )

    trip = models.ForeignKey(
        to=Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSIONS)
    img = models.ImageField(upload_to='images/notes', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        default=1, validators=[MaxValueValidator(limit_value=5, message='The rating can\'t be more than 5')])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} in {self.trip.city}'
