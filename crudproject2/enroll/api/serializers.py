from enroll.models import User 
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerialilizers):
    class Meta:
        model=User 
        fields=['id','name','email','password']