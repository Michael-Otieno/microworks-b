from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

  class Meta:
    model=Attendance
    fields=['id','full_names','email','machine_id','availability','time_in']