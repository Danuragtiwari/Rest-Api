from enroll.models  import User 
from enroll.serializers import UserSerializers 
from rest_framework import viewsets  

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
   serializer_class=UserSerializer






