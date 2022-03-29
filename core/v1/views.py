
from rest_framework import generics
from core.v1.serializers import ListSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated
from core.models import List, Item


class ListView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)


class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]