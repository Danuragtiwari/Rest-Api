# Function Based api_view:-
# This wrapper provide a few bits of functionality such as making sure you receive Request instances in your view,and adding context to response objects so that content negotiation can be performed.
# The wrapper also provide behaviour such as returning 405 method not allowed responses when appropriate and handling any parseError exceptions that occur when accessing request.data with malformed input.
# By default only GET methods will be accepted,other methods will respond with '405 method not allowed'
# @api_view()
#@api_view(['GET],'POST'.'PUT','DELETE')
# def function_name(request):
# ---
# ---
# 

# api_view:- 
# :-for GET method
# from rest_framework.decorators import api_view
# from restT_framework.response import Response 
# @api_view(['GET])
# def student_list(request):
#     if request.method=='GET':
#        stu=student.objects.all()
        # serializer=StudnetSerializer(stu,many=True) 
        # return Response(Serializer.data)
# 
# :-For post method
#from rest_framework.decorators import api_view
# from rest_framework.response import Response 
# from rest_framework import status
# @api_view(['POST])
# def student_create(request):
#    if request.method=='POST'
#       serializer=StudentSerializer(data=request.data)
#       if serilizer.is_valid():
#          serializer.save()
#          res={'msg':'Data Created'}
#          return Response(res,status=status.HTTP_201_CREATED)
#       return Response(Serializer.error,status=status.HTTP-400_BAD_REQUEST)    
# 
# Similarly:-MEthods=GET,POST,PUT,PATCH,DELETE
#
# Request:-REST framework's Request objects provide flexible request parsing that allows you to treat request with JSON data or other media types in the same way that you would normally deal with form data.
#request.data-request.data returns the parsed content of the request body.This is similar to the standard request.POST and request.FILES attributes except that:-
# *it includes all parsed content, including file and non-file inputs.
# *it supports parsing content of HTTP methods other than POST,meaning that you can access the content of PUT and PATCH requests.
# It supports REST frameworks flexible request parsing rather than just supporting form data,for examples you can handle incoming JSON data in the same way that you handle incoming form data
# request.method:-it return the euppercased string representations of the request's HTTP method
# BRower-based PUT,PATCH,and DELETE forms are transparently supported.

# request.query_params:-request.query_params is a more correctly named synonym for request.GET
# For clarity inside your code,we recommend using request.query_params instead of the Django's standard request.GEt,Doing so will help keep your codebase mre correct and aobvious -any HTTP method type may include query parameters,not just GET  requests.

# Response():-Rest framework supports HTTP content negotiation by providing a Response class which allows you to return content that can be rendered into multiple content types,depending on the client request.
# Response object sare intialized with data,which should consist of native python primitives,REST framework then uses standard HTTP content negotiation to determine how it should render the final response content.
# Response class simply provides a nicer interface for returning content-negotiated Web API responses,that can be rendered to mutliple formats.
# Syntax:-Response(data,status=None,template_name=None,headers=None,content_type=None)
# data:The unrenderd,serializeed data for the response.
# status: a status code for the response,defaults to 200.
# template_name: A template name to use only if HTMLRenderer or some other sutom template renderer is the accepted rendered for the response.
# headers:A dictionary of HTTP headers to use in the response.
# Content_type:the content typeof the response,typically,this will be set automatically by the renderer as determined by content negotiation,but there may be some cases where you need to specify the content type explicity.
# 
# 
# 
# # 
# 