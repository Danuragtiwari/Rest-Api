# Authentication:- 
# REST framework provides a nnumber of authentication schemes out of the box,and also  allows you to implement custom schemes.
# BasicAuthentication
# SessionAuthentication

# SessionAuthentication:-
# This authentication scheme uses Django's default session backend for authentication.Session authentication is appropriate for AJAX clients that are running in the same session context as your website.
# If successfully authenticated, Session Authentication provides the following credentials.
# request.user will be a Django User instance.
# request.auth will be None
# Unauthenticated responses that are denied permission will result in an HTTP 403 forbidden response.
# If you're using AJAX style API with SesssionAuthentication,you'll need to make sure you include a vslid CSRF token for any unsafe HTTP method calls,such as PUT,PATCH,POST,or DELETE requests.

# Permission:-
# Permissions are used to grant or deny access for different classes of the users to different parts of the API.
# Permission checks are always run at the very start of the views,before any code is allowed to proceed.
# Permission  checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be  permitted.

# Permission Classes:-
# Permission in the REST framework are always defined as a list of permission classes.
# AllowAny
# IsAuthenticated
# IsAdminUSer
# IsAuthenticatedOrReadOnly
# DjangoModelPermissions
# DjangoModelPermissionsOrAnonReadOnly
# DjangoObjectPermissions
# Custom Permissions


# AllowAny:-
# the AllowAny permission class will allow unrestricted access,regardless of it the request was authenticated or unauthenticated.
# this permission is not strictly required,since you can achieve the same result by using an empty list or tuple for the permission setting,but you may find it useful to specify this class because it makes the intention explicit.

# IsAuthenticated:-
# The IsAuthenticate permission class will deny permission to any unauthenticated user,and allow permission otherwise.
# This permission is suitable if you want your API to only be accessible to registered users.

# IsAdminUser:-
# The IsAdminUser permission class will deny permission to any user,unless user.is_staff is True in which ccase permission will be allowed.
# This permission is suitalbke if you want your API is accessible to a subset of trusted administrators.s

# IsAuthenticatedOrReadOnly:-
# The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request.Requests for unauthorised  users will onl be permitted if the request method is one of the 'safe' methods,GET,HEAD,or OPTIONS.
# This permission is suitable if you want to your API to allows read permissions to anonymous users,any only allow wirte permissions to authenticated users.

# DjangoModelPermissions:-
# this permission class ties into django's standard django.contrib.auth model permissions.This permission must only be applied to views that have a queryset property set.Authorization will only be granted if the user is authenticated and has the relevant model permissions assigned.
# POST requests require the user to have the add permission on the model.
# PUT and PATC?H requests require the user to have the change permission on the model.
# DELETE requests require the user to have the delete permission on the model.
# The default behaviour can alos be overridden to support custom model permissions.For example,you might want to includes a view model permission for GET requests.
# To use custom  model permissions,override DjangoModelPermissions and set the perms_map property.

# DjangoModelPermissionsOrAnonReadOnly:-
# Similar to DjangoModelPermissions,but also allows unauthenticated users to have read-only access to the API.


# DjangoObjectPermissions:-(#this having bugs so study but not implemented.)
# This permission class ties into Django's standard object permissions framework that allows per-object permissions on models.In order to use this permission class,You'll alos eed to add a permission backend that suppoerts object-level permissions, such as django-guardian.
# As with DjangoModelPermission ,this permission must only be applied to views that have a queryset property or get_queryset() method.Authorization will only be granted if the user is authenticated and has the relevant per-object permissions and relevant model permissions assigned.
# POST requests require the user to have the add permission on the model instance.
# PUT and PATCH requests require the user to have the change permission on the model instance.
# DELETE requests require the user to have the delete permission on the model instance.