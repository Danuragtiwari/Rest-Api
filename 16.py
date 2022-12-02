# ModelViewSet Class:-
# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions,by mixing in the beahvior of the various mixin classes.
# The actions provided by the odelViewSet class are list(),retrieve(),create(),update(),partial_update() and destroy(),you can use any of the standard attributes or method overrides provided by GenenricAPIVew
#ex:-
# class StudentViewSet(viewsets.ModelViewSet):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer