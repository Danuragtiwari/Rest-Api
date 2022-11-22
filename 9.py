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
    #  raise serializers.ValidationErrors('Seat Full')
    # return value 
 