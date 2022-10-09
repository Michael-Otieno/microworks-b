from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(max_length=255)
  last_name = serializers.CharField(max_length=255)
  email = serializers.EmailField(max_length=255)
  remotask_id = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=255,write_only=True)


  class Meta:
    model = User
    fields = ['first_name','last_name','email','remotask_id','password']


  def validate(self, attrs):
    email = attrs.get('email')
    remotask_id = attrs.get('remotask_id')

    if User.objects.filter(email=email).exists():
      raise serializers.ValidationError({"email":("Email is already in use")})
    
    if User.objects.filter(remotask_id=remotask_id).exists():
      raise serializers.ValidationError({"remotask_id":("The remotask id already exists")})
    return super().validate(attrs)

  def create(self, validated_data):
    return User.objects.create(**validated_data)

