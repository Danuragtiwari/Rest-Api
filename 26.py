# OrderingFilter:-
# The OrderingFilter class supports simple query parameter controlled ordering of the results.
# http://127.0.0.1:8000/studentapi/?ordering=name
# The client may also specify reverse orderings by prefixing the field name with '-',like so:
# http://127.0.0.1:8000/studentapi/?ordering=-name 

# Multiple ordering may also be specified:-
# http://example.com/api/users?ordering=account,username 

# its recommended that you explicitly specify which fields the API should allowing in the ordering filter.You can do this by setting an ordering_fields attribute on the view,like so:
# class StudentListView(generics.ListAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer 
#       filter_backends=[OrderingFilter]
#       ordering_fields=['name']  #we can add more in the list or '__all__'
