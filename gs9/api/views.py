from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view() #it include GET method by default
# def helllo_world(request):
#     return Response({'msg':'Heloo world'})

# @api_view(['POST']) 
# def helllo_world(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':'Heloo world POST method'})

@api_view(['POST','GET']) 
def helllo_world(request):
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'Heloo world POST method','data':request.data})
    if request.method=='GET':
        return Response({'msg':'Get method hai guys'})