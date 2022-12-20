from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=5 #ek page me 5 record at max
    limit_query_param='mylimit' #limit change to mylimit 
    offset_query_param='myoffset'
    max_limit=6 #maximum itna hi record dikhayega!