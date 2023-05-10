from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)        #text field gives us a box
    complete = models.BooleanField(default=False)               # gives a Check Box
    created = models.DateTimeField(auto_now_add=True)        #by default that current time will be set 

    def __str__(self):
        return self.title

    class Meta:
        # order_with_respect_to = 'user'
        ordering = ['complete']