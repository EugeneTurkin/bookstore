from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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
        book = self.get_object()
        book = book.change_count()
        return Response({"books left": book.count})
