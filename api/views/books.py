from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.models.books import Books
from api.serializers.books import BookSerializer, BookSerializerOut


class BookListCreateView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post', 'options']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request == 'GET':
            return BookSerializer
        return BookSerializerOut

    def get_queryset(self):
        filters = {}
        for field, value in self.request.query_params.items():
            filters[field] = value
        return Books.objects.select_related('author').filter(**filters)

    def list(self, request, *args, **kwargs):
        model_fields = [field.name for field in Books._meta.get_fields()]
        if any(field not in model_fields for field in list(self.request.query_params.keys())):
            return Response({"message": "Bad request. Verify the query params"}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Books.objects.select_related('author').all()
    serializer_class = BookSerializerOut
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
