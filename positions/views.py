from rest_framework import generics

from positions.models import Position
from positions.serializers import PositionSerializer


class PositionsAPIView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if kwargs.get('id'):
            return super().retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)
