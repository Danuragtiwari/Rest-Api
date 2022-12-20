# Pagination:-
# REST framework includes support for customizable pagination styles.This allows you to modify how large result sets are split into individual pages of data.

# PageNumberPagination
# LimitOFsetPagination
# CursorPagination

# Pagination Global Setting:-
# The  pagination style may be set globally,using the DEFAULT_PAGINATION_CLASS and PAGE_SIZE setting keys.
# REST_FRAMEWORK={
#     'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination',
#     'PAGE_SIZE':5,
# }

# Pagination Per View:-
# You can set the pagination class on an individual view by using the pagination_class attribute.
# class StudentList(ListAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer
#       pagination_class=PageNumberPagination

# PageNumberPagination:-
# This pagination style accepts a single number page number in the request query parameters.To enable the PageNumberPAgination style globally,use the following configuration,and set the PAGE_SIZE as desired:
# REST_FRAMWORK={'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':5}
# http://127.0.0.1:8000/studentapi/?page=3

# The PageNumberPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the PageNumberPagination class,and then enable your custom pagination class.
# django_paginator_class:- The django paginator class to use.Default is django.core.paginator.Paginator,which should be fine for most use cases.
# page_size:- A numeric value indicating the page size.If set, this overrides  the PAGE_SIZE setting.Defaults to the same value as the PAGE_SIZE settings key.
# page_query_param:-A string value indicating the name of the query parameter to use for the pagination control 
# page_size_query_param:-if set, this is a string value indicating the name of a query parameter that allows the client to set the pgae size on a per-request basis.Defaults to None,indicating that the client may not control the requested data.
# max_page_size:-If set,this is a numeric value indicating the maximuum allowable requested page size.This attribute is only valid if page_size_query_param is also set.
# last_page_strings:-A list or tuple of string values indicating values that may be used with the page_query_param to request the final page in the set.Defaults to ('last')
# template:-The name of the template to use when rendering pagination controls in the browsable API.May be overridden to modify the rendering style,or set to None to disable HTML pagination controls completely.Defaults to 'rest_framework/pagination/numbers.html' 
            
# PageNumberPagination:-
# class MyPageNumberPagination(PageNumberPagination):
#      page_size=5 
#      page_size_query_param='records'
#      max_page_size=7 
# class StudentList(ListAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializer
#      pagination_class=MyPageNumberPagination
