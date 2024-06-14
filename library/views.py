from rest_framework import viewsets
from library.models import Book
from library.permissions import IsAdminOrIfAuthenticatedReadOnly
from library.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
