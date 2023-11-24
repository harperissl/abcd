from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255, default='')
    number_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
