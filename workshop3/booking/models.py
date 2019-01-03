import datetime

from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=128)
    volume=models.IntegerField()
    projector_availability=models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.name,self.id)

class Booking(models.Model):
    booking_date=models.DateField(default=datetime.date.today)
    comment=models.TextField(blank=True,null=True)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
