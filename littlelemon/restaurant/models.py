from django.db import models
from django.core import validators

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(
        primary_key=True,
        validators=[validators.MinValueValidator(0)]
    )
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators= [validators.MinValueValidator(1), validators.MaxValueValidator(999999)]
    )
    booking_date = models.DateTimeField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.SmallIntegerField(
        validators= [validators.MinValueValidator(0), validators.MaxValueValidator(1000)]
    )
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return self.get_item()
    
