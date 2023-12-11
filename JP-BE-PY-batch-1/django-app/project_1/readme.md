1. APIView class doesn't support queryset and serialzier_class i.e it doesn't coupled with django model. Generics and Viewset support queryset i.e coupled with django model
2. APIView class do support permission_class same like Generics and Viewset
3. APIView and Generics doesn't enforce creating Restful APIs while viewset does
4. APIView and Generics use urlpatterns while viewset uses router
5. ModelViewSet lets us specify just one serializer, you cannot defined input and output separate serializer without overriding the method get_serializer_class
example
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all() 
    read_serializer_class = ProjectReadSerializer 
    write_serializer_class = ProjectWriteSerializer

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

6. override: 
    a. override whole API main function (i.e create, update) on viewside
    b. override only create, update method that alraedy have the validated data on serializer side.
    c. override validate method of custom validation on serializer side