# Filtering:-
# The simplest way to filter the queryset of any view that subclasses GenericAPIView is to override the .get_queryset() method.
# 


# Generic Filtering:-
# REST framework also includes supoort for generic filtering backends that allow you to easily construct complex searches and filters.


# DjangoFilterBackend:-
# The django-filter library includes a djangoFilterBackend class which supports customizable field filtering for rest framework.
# To use DjangoFilterBackend,first install django-filter 
# pip install django-filter 
# then add 'django_filters'  to django's Installed_apps:
# INSTALLED_APPS=['django_filters',]
# https://django-filter.readthedocs.o/en/latest/index.html

# Settings.py
# REST_FRAMEWORK={
    # 'DEFAULT_FILTER_BACKENDS':
        # ['django_filters.rest_framework,DjangoFilterBackend']
# }


# Per View Setting 
# You can set the filter backends on a per-view,or per-viewset basis,using the GenericAPIView class-based views.
# from django_filters.rest_framework import DjangoFilterBackend
# class StudentListView(ListAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializer
#      filter_backends=[DjangoFilterBackend] 

# DjangoFilterBackend:-
# If all you need is simple equality-based filtering,you can set a filterset_fields attribute on the view,or viewset,listing the set of fields you wish to filter against.
# class StudentList(ListAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer 
#       filter_backends=[DjangoFilterBackend]
#       filterset_fields=['name','city']
