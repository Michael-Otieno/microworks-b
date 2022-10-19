from re import A
from .models import Attendance
from .serializers import AttendanceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.generics import GenericAPIView 
from rest_framework import generics

# Create your views here.

class AttendanceList(generics.GenericAPIView):
  '''
  list of all in attendance or add attendance
  '''
  serializer_class = AttendanceSerializer
  def get_queryset(self):
    return Attendance.objects.all()

  def get(self,request,format=None):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer = AttendanceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(generics.GenericAPIView):
  """
  Retrieve, update or delete someones attendance details
  """
  serializer_class = AttendanceSerializer
  permission_classes=(IsAdminOrReadOnly,)  
  def get_object(self, pk):
    try:
      return Attendance.objects.get(pk=pk)
    except Attendance.DoesNotExist:
      raise Http404

  def get(self,request,pk,format=None):
    attendance = self.get_object(pk)
    serializer=AttendanceSerializer(attendance)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    attendance=self.get_object(pk)
    serializer=AttendanceSerializer(attendance,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    attendance = self.get_object(pk)
    attendance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
