from django.db import models
import datetime as dt
# Create your models here.


# location model
class Location(models.Model):
    name = models.CharField(max_length=30)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
