# Custom Permissions:-  
# To implement a custom permission,override BasePermission and implement either,or both of the following methods:
# has_permission(self,request,view)
# has_object_permission(self,request,view,obj)
# The methods should return True if the request should be granted access,and False otherwise.  
# Custom Permissions:
# create custompermissions.py
#class MyPermission(BasePermission):
#   def has_permission(self,request,view):