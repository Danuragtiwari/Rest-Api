# Concrete View Class:-
# The following classes are the concrete generic views.If  you're using generic views this you will be working atunless you need havliy cutomized behavior.
# The view classes can be imported from rest_framework.generic.
#ListAPIView:-ListCreateAPIView
# CreateAPIView:-REtrieveUpdateAPIView
# RetrieveAPIView:-RetrieveDestroyAPIView
#UpdateAPIView,DesktroyAPIView:-RetrieveUpdateDestroyAPIView 
# # 

# ListAPIView:-It is used for read-only endpointd to represent a collections of model instances.It provides a get method handler.
# Extends:-GenericAPIView,ListModelMixin
# Ex:-
#from rest_framework.generics import ListAPIView
# class StudentList(ListAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializer()
# 

# CreateAPIView:-It is used for create-only endpoints,it provides a post method handler.
# Extends:-GenericAPIView,CreateModelMixin
# Ex:-
# from rest_framework.genenrics import CreateAPIView
# class StudentCreate(CreateAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer 
# 

# RetrieveAPIView:-
# It is used for read-only endpoints to represent a single model instance.It provides a get method handler.
# Extends:-GenericAPIVIiew,RetrieveModelMixin 

# ex:-
# from rest_framework.generics import RetrieveAPIView
# class StudentRetrieve(RetrieveAPIView):
#       query=Student.objects.all()
#       serializer_class=StudentSerializer

# UpdateAPIView:-
# it is used for update only endpoints for single model instance.It provide put and patch method handlers.
# Extends:-GenericAPIView,UpdateModelMixin
# ex:-
# from rest_framework.generics import UpdateAPIView
# class StudentUpdate(UpdateAPIView):
#       queryset=Student.objects.all()
#       serializer=class=StudentSerializer

# DestroyAPIView:-It is used for delete only endpoints for single model instance.It provides a delete method handler.
# Extends:-GenericAPIView,DestroyModelMixin
# ex:-
#  
# from rest_framework.generics import DestroyAPIView
# class StudentDestroy(DestroyAPIView):
#       queryset=Student.objects.all()
#       serializer=StudentSerializer

# ListCreateAPIView:-It is used for read-write endpoints to represent a collection of model instances.It provides get and post method handlers.
# Extends:-GenericsAPIView,ListModelMixin,CreateModelMixin

# from rest_framework.generics import ListCreateAPIView
# class StudentListCreate(listCreateAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer 

# RetrieveUpdateAPIView:-It is used for read or update endpoints to reresent a single model instance.It provudes get,put,and patch method handlers.
# Extends:-GenericAPIView,RetrieveModelMixin,UpdateModelMixin

# ex:-
# from rest_framework.generics import RetrieveUpdateAPIView 
# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer

# RetrieveDestroyAPIView:-IT is used for read or delete endpoints to represent asingle model instance.It provifdes get  and delete method handlers.
# Extends:-GenericAPIView,RetrieveModleMixin,DestroyModelMixin

# ex:-
# from rest-framework.generics import RetrieveDestroyAPIView
# class StudentRetriveDestroy(RetireveDestroyAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer

# RetrieveUpdateDestroyAPIView:-It is used for read write delete endpoints to represent a sigle model instance .it provides get,put,patch and delete method handlers.
# Extends:-GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# ex:-
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer

