# ModelViewSet 
from .models import Student
from .serializers import StudentSerializer 
from rest_framework import viewsets  
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from api.customauth import CustomAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
 
    

   