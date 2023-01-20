from rest_framework import viewsets
from cliente.api import serializers
from cliente import models


class ClienteViewSet(viewsets.ModelViewSet):
    # queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

    def get_queryset(self):
        cpf = self.request.query_params.get('cpf', None)
        return models.Cliente.objects.filter(cpf=cpf)

    def create(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).create(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).destroy(request, *args, **kwargs)
