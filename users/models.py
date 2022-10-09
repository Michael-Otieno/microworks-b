from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  remotask_id = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  # confirm_password = serializers.CharField(max_length=255, min_length=8, write_only=True)
  class Meta:
        ordering = ['email']