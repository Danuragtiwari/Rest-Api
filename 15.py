#ViewSet:- 
# Django REST framework allows you to combine the logic for a set of related views in a single class called aViewSet
# There are two main advantages of using aViewSet over using a View class.
# Repeaterad logic can be combined into a single class.
# By using routers,we no longer need to deal with wiring up the URL conf ourselves.

# ViewSet Class:-
# A viewSet class is simply a type of ckass-based View,that does not provide any method handlers such as get(),or post(),and instead provides actions such as list() and create().
# list():- Get all records
# retrieve():-Get single record
# create():-Create/Insert record
# update():-Update Record completely
# partial_update():-Update Record partially
# destroy():-Delete Record


# ViewSet class:-
# from rest_framework import viewsets
# class StudentViewSet(viewsets.ViewSet):
#      def list(self,request):
#      def create(self,request):
#      def retrieve(self,request,pk=None):
#      def update(self,request,pk=None):
#      def partial_update(self,request,pk=None):
#      def destroy(self,request,pk=None):

# During dispatch,the following attributes are availabel on the ViewSet:-
# basename:-The base to use for the URL names that are created.
# action:-the name of the currect action(e.g.,list,create)
# detail:-Boolean indicating if the currect action is configured for a list or detail view.
# suffix:- The display suffix for the viewset type-mirrors the detail attribute.
# name:-the display name for the viewset,this argument is mutuallly exclusive to suffix
# description:-The display description for the individual view of a viewset.

# ViewSet-URLConfig:-
# from djangp.urls import path,include
# from api import views
# from rest_framework.routers import DefaultRouter
# 
# router=DefaultRouter()
# router.register('studentapi',views.StudentViewSet,basename='student')

# urlpatterns=[
    # path('',include(router.urls)),
# ]