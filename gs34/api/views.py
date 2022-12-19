from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend #it is for local filters
# Create your views here.
class StudentList(ListAPIView):
    queryset =Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend] #It is for local filters
    filterset_fields=['city','name']
    