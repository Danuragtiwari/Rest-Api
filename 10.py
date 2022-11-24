# Modelserializer class
# 
# The modelserializer class provides a shortcut that lets you automatically create a serializer class with fields that correspond to the model fields.
# the modelSerializer class is the same as a regular serializer class,except that:-
# it will automatically generate a set of fields for you ,based on the model.
# It will automatically generate validators for serializer,such as unique_together validators.
# It includes simple default implementations of create() and update().

# Create ModelSerializer Class

# Create s separate serializers.py to write al serializers 
# 
# from rest_framework import serializers
# class StudentSerailizer(serializers.ModelSeriaizer):
#       class Meta:
#             model=Student
#             fields=['id','name','roll','city']
# fields='__all__'
# exclude=['roll'] 

# Create modelSerializer class:-
# from rest_frramework import serialisers
# class StudentSerializer(serializers.ModelSerializer):
#       name=serializers.CharField(read_only=True)
#       class Meta:
    #         model=Student
    #         fields=['id','name','roll','city']
#  
# class StudentSerializer(serializers.ModelSerializer):
#      
#       class Meta:
    #         model=Student
    #         fields=['id','name','roll','city']
    #         read_only_fields=['name','roll']
    
#Validation in ModelSerialization 
# 
# from rest_framework import serializers
# class StudentSerializer(serializers.ModelSerializer):
#       class Meta:
#            model=Student
#            fields=['id','name','roll','city'] 
#       def validate_roll(self,value):
# if value>=200:
    # raise serializers.ValidationError('Seat Full')
# return value 
# 
# 
# 
# 