from rest_framework import generics

from users.models import Account
from users.serializers import AccountSerializer


class AccountAPIView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        if kwargs.get('id'):
            return super().retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)