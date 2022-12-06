# TokenAuthentication:-
# This authentication scheme uses a simple token-based HTTP Authentication scheme.Token Authentication is appropriate for client-server setups,such as native desktop and mobile clients.
# To use the TokenAuthentication Scheme you will need to configure the authentication classes to include TokenAuthentication,and Additionally include rest_framework.authtoken in your INSTALLED_APPS setting: INSTALLED_APPS=[..,'rest_framework.authtoken']
# Note: Make sure to run manage.py migrate after changing your settings,the rest_framework.authtoken app provides Django database migrations.
# If successfully authenticated,TokenAuthentication provides the following credentials.
# request.user will be django user instance,request.auth will be a rest_framework.authtoken.models..Token instance.
# Unauthenticated responses that are denied permission will result in an HTTP 401 unauthorized response will an appropriate WWW-authenticate header.For example:- WWW-Authenticate:Token
# The http command line tool may be useful for testing token authenticated APIs,for example:-http htttp://127.0.0.0.1:8000/studentapi/'Authorization:Token 9944b09199c62bcf9418ad846dd0e4bbdfe6ee4b'
# Note:-If you use TokenAuthentication in production you must ensure that your API is only available over https.

# Generate Token:-
# using Admin Application:-
# Using django manage.py command:- python manage.py drf_create_token<username> ..this command will return APIToken for the given user or Creates a Token if doesn't exist for user.
# By exposing an API endpoint
# Using Signals

# How client can ask/create token :-
# When using tokenAuthentication,yu may want to provide a mechanism for clients to obtain a token given the username and password.
# REST framework provides a built-in view to provide this behaviour.To use it,add the obtain_auth_token view to your URLconf:
# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns=[path('gettoken/',obtain_auth_toekn)]
# The obtain_auth_token view will return a JSON response when valid username and password fields are posted to the view using form data or JSON:
# example:- http POST http://127.0.0.1/gettoken/username='name'password='password'
# {'token':'12365yfsfsfaf'} in this form we will get

# it also generates token if the token is not generated for the provided user.