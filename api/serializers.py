from rest_framework import serializers

from students.models import User

class UeserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','email',]

 
