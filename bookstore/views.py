from django.db import IntegrityError
from django.db.models import F
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bookstore.exceptions import OutOfStock
from bookstore.models import Author, Book
from bookstore.serializers import AuthorSerializer, BookSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the bookstore index.")


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        try:
            queryset = Book.objects.select_for_update().filter(id=pk).update(count = F("count")  - 1)
        except IntegrityError as e:
            raise OutOfStock from e
        book = self.get_object()
        return Response({"books left": book.count})
