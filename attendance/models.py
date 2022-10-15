import email
from django.db import models

# Create your models here.

class Attendance(models.Model):
  full_names = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  machine_id = models.CharField(max_length=255)
  availability = models.TextField()
  time_in = models.DateTimeField(auto_now_add=True)

  class Meta:
    get_latest_by='time_in'
