from django.db import models
from django.contrib.auth.models import User


# Planning an event within the group
# Note for later: Maybe for USERS give them profile pictures in a sub class
class Events(models.Model):
    name = models.CharField(max_length=30)
    date_planned = models.DateField()
    location = models.CharField(max_length=100)
    cost_rating = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)
    # I could add details to this "toString method", but the admin dashboard uses this for the object name

    def __str__(self):
        return "" + str(self.name)

    def details(self):
        return "" + str(self.name) + " " + str(self.manager) + " " + str(self.members) + " " + str(self.id)


# Setting up photo albums of specific groups
class Memories(models.Model):
    image = models.ImageField(blank=False)
    caption = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "" + str(self.name)


# Organizing sets of friends to do everything within it
class Groups(models.Model):
    name = models.CharField(max_length=30)
    # icon = models.ImageField()
    events = models.ManyToManyField(Events, blank=True, default=None)
    memories = models.ManyToManyField(Memories, blank=True, default=None)
    members = models.ManyToManyField(User, related_name="people")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin")

    def __str__(self):
        return "" + str(self.name)
