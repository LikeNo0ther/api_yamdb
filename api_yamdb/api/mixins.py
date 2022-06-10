from rest_framework import mixins, viewsets


class ListDeleteViewSet(mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class ListCreateDestroyUpdateViewset(mixins.ListModelMixin,
                                     mixins.DestroyModelMixin,
                                     mixins.CreateModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     viewsets.GenericViewSet):
    pass
