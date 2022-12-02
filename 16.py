# ModelViewSet Class:-
# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions,by mixing in the beahvior of the various mixin classes.
# The actions provided by the odelViewSet class are list(),retrieve(),create(),update(),partial_update() and destroy(),you can use any of the standard attributes or method overrides provided by GenenricAPIVew
#ex:-
# class StudentViewSet(viewsets.ModelViewSet):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer

# ReadOnlyModelViewSet Class:-
# The ReadOnlyModelViewSet class also inherits from GenericAPIVIew.As with ModelViewSet it also includes implementations for varios actions,but unlike ModelViewSet only proivdes the'Read-only' actions,list() aand retrieve().YOu canuse any of the standard attributes and method overrides available to GenericAPIView.

# ex:-
# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#      queryset=Student,objects.all()
#      serializer_class=StudentSerializer
