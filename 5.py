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

# Serializers:-In django REST framework,serializers are responsible for converting complex data such as Querysets and model instance to native Python datatypes(called serialization) that can then be easily rendered into JSON,XML or orther content types which is understandable by frontend.
#It is also responsible for deserialization  which means it allows parsed data to be converted back into complex types,after first validating the incoming data.
# serialization
# Deserialization

# Serializer Class:- it is very similar to a django Form and modelForm class and includes similar validation flags on the various fields,such as required,max_length and default.Django Rest-framework(DRF) provides a serializer class which gives you a powerful,generic way to control the output of your responses as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

# How to Create Serializer Class
# Create a separate seriealizers.py file to write all serializers 
# from rest_framework import serializers
# class 
# 
# 
# 
