from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Passenger(models.Model):
    id           = models.AutoField(primary_key=True, unique=True)
    name         = models.CharField(max_length=30)
    passport     = models.IntegerField(blank=True, null=True)
    ticket       = models.IntegerField(blank=True, null=True)
    dem_register = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Flight(models.Model):
    id             = models.AutoField(primary_key=True, unique=True)
    destination    = models.CharField(max_length=50)
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    terminal       = models.CharField(max_length=1,
                                      validators=[RegexValidator(r'^[AB]$', 'Можна вводити лише символи A та B')])
    max_capacity   = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.destination}"


class Registration(models.Model):

    WANTED_CHOICES = (
        (0, 'Not wanted'),
        (1, 'Wanted')
    )

    id            = models.AutoField(primary_key=True, unique=True)
    passenger_id  = models.ForeignKey('Passenger', on_delete=models.CASCADE, blank=True, null=True)
    flight_id     = models.ForeignKey('Flight', on_delete=models.CASCADE, blank=True, null=True)
    visa          = models.IntegerField(blank=True, null=True)
    luggage_price = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    price         = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    wanted        = models.IntegerField(choices=WANTED_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.passenger_id}"


class Luggage(models.Model):
    id              = models.AutoField(primary_key=True, unique=True)
    registration_id = models.ForeignKey('Registration', on_delete=models.CASCADE, blank=True, null=True)
    weight          = models.DecimalField(decimal_places=2, max_digits=5)


class Interpol(models.Model):
    id           = models.AutoField(primary_key=True, unique=True)
    name         = models.CharField(max_length=30)
    dem_register = models.BigIntegerField(blank=True, null=True)