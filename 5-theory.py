# Django REST Framework:-(Serializer and Serializer Class)
# Python has a built in package called json,which is used to work with JSON data.
# dumps(data):-This is used to convert python object into json string.
# Example:- To use json package first we have to import it.
# import json
# python_data={'name':'slim','roll':1}
# json_data=json.dumps(python_data)
# print(json_data)  #{"name":"slim","roll":1}

# loads(data):-This is used to parse JSON string.
# Example:-
# import json
# json_data={'name':'sonam','id':1}
# parsed_data=json.loads(json_data)
# print(parsed_data) #{'name':'sonam','id':1}

# Serializers:-In django REST framework,serializers are responsible for converting complex data such as Querysets and model instance to native Python datatypes(called serialization) that can then be easily rendered into JSON,XML or other content types which is understandable by frontend.
#It is also responsible for deserialization  which means it allows parsed data to be converted back into complex types,after first validating the incoming data.
# serialization
# Deserialization

# Serializer Class:- it is very similar to a django Form and modelForm class and includes similar validation flags on the various fields,such as required,max_length and default.Django Rest-framework(DRF) provides a serializer class which gives you a powerful,generic way to control the output of your responses as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

# How to Create Serializer Class
# Create a separate seriealizers.py file to write all serializers 
# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):  #class name(serializers.Serializer)
#  name=serializers.CharField(max_length=100)
# roll=serializers.IntegerField()
# city=serializers.CharField(max_length=100)



# Now make models.py
# from django.db import models 
# class Student(models.Model):
# name=models.CharFiedl(max_length=100)
# roll=models.IntegerField()
# city=models.CharField(max_length=100)

# Run makemigrations and migrate the command
# table or models abject we have to convert it to in json formate.
# Complex Data type--(serialization)-->Python Native DataType--(Render into Json)-->Json Data

# The process of converting complex data such as querysets and model instances to native python datatypes(Boolean,Numbers,Strings,Bytes(jpeg images),List,....) are called as Serialization in DRF.
# Creating model instance stu
# stu=Student.objects.get(id=1)
# Converting model instannce stu to python Dict/Serializing Object
# serializer=StudentSerializer(stu)
# Similarly for Query Set
# Creating Query Set
# stu=Student.objects.all()
# Converting Query set stu to List of python Dict/Serializing Query set
# serializer=StudentSerializer(stu,any=True)
# To get or print serializer data ,print(serializer.data)

# JSONRenderer
# This is used to render Serialized data into JSON which is understandable by Front End
# Importing JSONRenderer
# from rest_framework.renderers import JSONRenderer

# Render the Data into Json
# json_data=JSONRender().render(serializer.data)

# JsonResponse()
# JsonResponse(data,encoder=DjangoJSONEncoder,safe=True,json_dumps_params=None,**kwargs)
# An HttpResponse subclass that helps to create a JSON-encoded response.It inherits most behaviour from its superclass with a couple differences.
# its differences:-
# it default content-type header is set to application/json
# the first parameter,data,should be dict instance,if the safe parameter is set to False it can be any JSON-serializable object.
# The encoder,which defaults to django.core.serializers.json.DjangoJSONEncoder,will be used to serialize the data.
# The safe boolean parameter defaults to True,if it set to false,any object can be passed for serialization(otherwise only dict instances are allowed).If safe is True and a non-dict object is passed as the first argument,a TypeError will be raised.