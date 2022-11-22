# Validation  
# 1.Field level validation:- We can specify custom field-level validation by adding validate_fiedlName methods to your serualuzers subclass. These are similar to the clean_fieldName methods on django forms.validate_fieldame methods should return the validated value or raise a serializers.ValidationError
# syntax:- def validate_fieldame(self,value)
# Example:-def validate_roll(self,value)
# where,value is the field value that requires validation.

# from rest_framework import serializers
#class StudentSerializer(serializers.Serializer):
# name=serializers.CharField(max_length=100)
# roll=serializers.IntergerField() 
# city=serializers.CharField(max_length=100)
# def validate_roll(self,value): this method is automatically invoked when is_valid() method is called
# if value>=200:
    #  raise serializers.ValidationError('Seat Full')
    # return value 
 

# Object Level Validation:-when we need to do validation that requires access to multiple fields we do object level validation by adding a method called validate() to Serialize subclass.

# It raises a serializers.ValidationError if  necessary,or just return the validated values.
# Syntax:-def validate(self,data)
# Example:-def validate(self,data)
# where,data is a dictionary of field values.

# Exampple:-
# from rest_framework import serializers 
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)
#     def validate(self,data): #data is a python dictonary of field values.
#         nm=data.get('name)
#         ct=data.get('city')
#         if nm.lower()=='rohit' and ct.lower()!='ranchi':
#             raise serializers.ValidationError("City must be ranchi")
#         return data


# Validators:-
# Most of the time,we'r dealing with validation in REST framework you will simply be relying on the default field validation,or writing explicit validation methods on serializer or field classes.
# However,sometimes you will want to place your validation logic into reusable components,so that it can easily be reused throughout yours codebase,this can be achieved by using validator function and validator classes.
# its advantages:-
# it introduces a proper separations of concerns making your code behaviour more obvious.
# it is easy to switch between using shortcut ModelSerializer classes and using explicit Serializer classes.Any validation behavior being used for ModelSerializer is simple to replicate.
# Pring the repr() of a serializer instance will show you exactly what validation rules it applies.there's no extra hidden validation behaviour being called on the model instance.
# when you'r using ModelSerializer all of this is handled automatically for you,if you want to drop down to using Serializer classes instead,then you need to define the validation rules explicitly.

# from rest_framework import serializers
# def starts_with_r(value):
#    if value['0'].lower()!='r':
#       raise serializers.ValidationError('Name should start with R')
# class StudentSerializer(serializers.Serializer):
#       name=serializers.CharField(max_length=100,validators=[starts_with_r])
#       roll=serializers.IntegerField()
#       city=serializers.CharField(max_length=100)
