from django.db import models
from django.contrib.auth.models import User
import datetime

class Room(models.Model):
    name=models.CharField(max_length=200)
    floor=models.CharField(max_length=200)
    room_number=models.CharField(max_length=200)
    available=models.BooleanField(default=False)


    def str(self):
        return f"{self.name}, room: {self.room_number}, floor: {self.room_number}"



class Meeting(models.Model):
    customer = models.ForeignKey(User, related_name='Meet_created', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(default=datetime.datetime.now)
    duration = models.IntegerField(default=1)
    room=models.ForeignKey(Room,related_name='Room_not_available',on_delete=models.CASCADE)

    def str(self):
        return f"title:  {self.title} date: {self.date} "