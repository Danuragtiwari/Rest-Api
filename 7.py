# Deserialization:-Serializers are also responsible for deserilaization which means it allows parsed data to be converted back into complex types after first validating the incoming data.
# Serialization:- Complex data type ---(serialization)-->Python Native Datatype--(Render into Json)-->Json Data
# Deserialization:-Json Data--(parse Data)-->Python Native Datatype--(De-serialization)-->Complex DataType

# BytesIO():-A stream implementation using an in-memory bytes buffer.It inherits BufferedIOBase.The buffer is discarded when the close() method is called.
# import io
# stream=io.BytesIO(json_data)

# JSONParser():-this is used to parse json data to python native data type.
# from rest_framework.parsers import JSONParser
# parsed_data=JSONParser().parse(stream)

# De-serialization allows parsed data to be converted back into complex types after first validating the incoming data.

# Creating Serializer Object
# serializer=StudentSerializer(data=parsed_data)
# Validated Data
# serializer.is_valid()
# serializer.validated_data
# serializer.errors

# serializer.validated_data --this is the valid data.

# Create Data/Insert Data

# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):
# name=serializers.CharField(max_length=100)
# roll=serializers.IntegerField()
# city=serializers.CharField(max_length=100)
# 
# def create(self,validate_data):
# return Student.objects.create(**validate_data)
# 