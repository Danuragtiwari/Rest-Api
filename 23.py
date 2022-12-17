# Throttling:-
# It is similar to permissions,in that it determines if a request should be authorized.Throttles indicate a temporary state,and are used to control the rate of requests that clients can make to an API.Your API might have a restrictive throttle for unauthenticated requests and a less restrictive throttle for authenticated requests.

# The default throttling policy may be set globally ,using the 
# DEFAULT_THROTTLE_CLASSES and DEFAULT_THROTTLE_RATES settings .For example:-
# REST_FRAMEWORK={'DEFAULT_THROTTLE_CLASSES':['rest_framework.throttling.AnonRateThrottle','rest_framework.throttling.USerRateThrottle'],
# 'DEFAULT_THROTTLE_RATES':{'anon':'100/day','user':'1000/day'}}  #the rate descriptions used in here may include second,minutes,hour or days

# AnonRateThrottle:-
# IT will only ever throttle unauthenticated users.The IP address of the incoming requests is used to generate a unique key to throttle against.The allowed request rate is determined from one of the following (in order of the preference.)
# the rate property on the class,which may be provided by overriding AnonRateThrottle and setting the property.
# The DEFAULT_THROTTLE_RATES['anon'].setting 
# AnonRateThrottle is suitable if you want to restrict the rate of requests from unknown sources. 

# UserRateThrottle:-
# The UserRateThrottle will throttle users to given rate of requests across the API.The user id is used to generate a uique key to throttle against.Unauthenticated requests will fall back to using the IP address of the incoming request to generate a unique key to throttle against.
# the allowed request rate is determined from one of the following(in order of preference)
# The rate property on the class,which may be provided by overriding UserRate Throttle and setting the property.
# The DEFAULT_THROTTLE_RATES['user]setting.

# ScopedRateThrottle:-
# It's class can be used to restrict access to specific parts of the API.This throttle will only be applied if the view that is being accessed included a throttle_scope property.The unique throttle key will then be formed by concatenating the 'scope' of the request with the unique user id or IP address.