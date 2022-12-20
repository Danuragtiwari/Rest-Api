from rest_framework.pagination import PageNumberPagination 

class MyPageNumberPagination(PageNumberPagination):
    page_size=5 
    page_query_param='p' #yese to page hi hota h by default ,take p=last
    page_size_query_param='records'  #url/?p=1&records=7 check it
    max_page_size=7
    last_page_strings='end' #p=last change last to end