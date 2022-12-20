# SearchFilter:-
# The SearchFilter class supports single query parameter based searching and is based on the django admin's search functionality.
# The SearchFilter class will only be applied if the view has a search_fields attribute set.The search_fields attribute should be a list of names of text type fields on the model,such as CharField or TextField.


# use
# from rest_framework.filters import SearchFilter 
# class StudentListView(ListAPIView): 
#       queryset=Student.objects.all()
#       serializer_class =StudentSerializer 
#       filter_backends=[SearchFilter ]
#       search_fields=['city']
 
# http://127.0.0.1:8000/studentapi/?search=Ranchi 

# '^' Starts-with search 
# '=' Exact matches
# '@' Full-text search.(Currently only supported Django's PostgreSQL backend)
# '$' Regex search

# Example:-
# search_fields=['^name',]
# http://127.0.0.1:8000/studentapi/?search=r