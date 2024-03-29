# ModelViewSet 
from .models import Student
from .serializers import StudentSerializer 
from rest_framework import viewsets  
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticatedOrReadOnly]
   
