# Authentication:-
# Third Party Packages:
# JSON web Token Authentication:-
#JSON web token is a fairly new standard which can be used for token-based authentication.unlike the built-in TokenAuthentication scheme,JWT Authentication doesn't need to use a database to validate a token.
# please refers:- google for more info

#Simple JWT:-
# Simple JWT provides a JSON web Token Authentication backend for the Django Rest Framework.It aims to cover the most common use cases of JWT's by offering a conservative set of default features.It also aims to be easily extensible in case a desired features is not present.
# https://django-rest-framework-simplyjwt.readthedocs.io/en/latest/

# How to install Simple JWT
# pip install djangorestframework-simplejwt

# How to configure Simple JWT:-
# settings.py :- it is globlly define for every views
#  REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication',)}

# urls.py
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 
# urlpatterns=[
# path('gettoken',TokenObtainPairView.as_view(),name='token_obtain_pair'),
# path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
# ]


# To verify:-
# You can also include a route for simple JWT's Token VerifyView if you wish to allow API users to verify HMAC-signed tokens without having access to your signing key.
# urls.py
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# urlpatterns=[
# path('gettoken/',TokenObtainView.as_view(),name='token_obtain_pair'),
# path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
# path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
# ]

# JWT Default Settings:-
# from datetime import timedelta 
# SIMPLE_JWT={'ACCESS_TOKEN_LIFETIME':timedelta(minutes=5),'REFRESH_TOKEN_LIFETIME':timedelta(days=1),'ROTATE_REFRESH_TOKENS':False,'BLASKLIST_AFTER_ROTATION;:True,
# 'ALGORITHM':'HS256','SIGNING_KEY':settings.SECRET_KEY,'VERIFYING_KEY':None,'AUDIENCE':None,'AUTH_KEADER_TYPES':('Bearer',),'USER_ID_FIELD':'id','USER_ID_CLAIM':'user_id','AUTH_TOKEN_CLASSES':('rest_framework_simplejwt.tokens.AccessToken',),'TOKEN_TYPE_CLAIM':'token_type','JTI_CLAIM':'jti','SLIDING_TOKEN_REFRESH_EXP_CLAIM':'refresh_exp','SLIDING_TOKEN_LIFETIME':timedelta(minutes=5),}

# ACCESS_TOKEN_LIFETIME:- a datetime.timedelta object which specifies  how long access tokens are valid.

# REFRESH_TOKEN_LIFETIME:- A datetime.timedelta object which specifies how long refresh tokens are valid.
 
# Use JWT  
# Get Token 
# from urls write,urlpatterns=[path('gettoken/',)]
# http POST http://127.0.0.1:8000/gettoken/ username='user1 password='Danurag23@'
# for verify Token
# http POST http://127.0.0.1:8000/verifytoken/ token='uddhcvuygruygkydvghdggvkdgvmdhgkuy336287trwf ghegfjygeyfgehj'
# we get OK for verify else bad request .
# Refresh Token
# http POST http://127.0.0.1:8000/refreshtoken/ refresh='qpokfwbkhdghjbscvgv661218y928y98qhwui78'


# Permission Classes:- Permission in REST framework are always defined as alist of permission classes. 
# AllowAny 
# IsAuthenticated
# IsAdminUser
# IsAuthenticatedOrReadOnly
# DjangoModelPermissions
#DjangoModelPermissionsOrAnonReadOnly
# DjangoObjectPermissions 
# Custom Permissions


# to get 
#  http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMjk0NTY5LCJpYXQiOjE2NzEyOTMxMDIsImp0aSI6ImQxYmNlMTQ3YTEyZTRhMTA5ZjA0NWY1Njc5ZDc0NjQxIiwidXNlcl9pZCI6MX0.OKyXrxPKnO66u38-WSVZ88zKUmdqIN29x4PNiTfZIDs'