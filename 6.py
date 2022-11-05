# From rest_framework import serializers 
# class StudentSerializer(Serializers.Serializer):
# name=serializers.CharField(max_length=100)
# roll=serilaizers.IntegetField()
# city=serilaizers.CharField(max_length=100)
# 
# Serializer fields handle converting between primitive values and internal datatypes.they also deal with validating input values,as well as retrieving and setting the values from their parent objects.
# syntax:
# from rest_framewrok import serializers
# serializers.Field_Name()

# Examples:-
# from rest_framework import serializers
# serializers.CharField()

# CharField=A text representation ,optionally validates the text to be shorter than max_length and longer than min_length.
# Syntax:-CharField(max_length=None,min_length=None,allow_blank=False,trim_whitespace=True)
# IntegerField=An interger Respresentstion,syntax:-IntegerField(max_value=None,min_value=None)
# floatField=A floating point representation,syntax:-FloatField(max_value=None,min_value=None)
# DecimalField:-A decimal representation,represented in python by a decimal instance.
# syntax:-DecimalField(max_digits,decimal_places,coerce_to_string=None,max_value=None,min_value=None)
# 
# Slugfield=A regexField that validates the input againts the pattern,syntax:-SlugField(max_length=50,min_length=None,allow_blank=False)

# Core Arguments:-
# label:-A short text string that may be used as the name of the field in html form fields or others elements.
# Validators:-
# Error_messages:-
# help_text:-
# required:-
# initial:-
# style:-