from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.models import Authors
from api.serializers import AuthorSerializer


# Authors
class AuthorListCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        filters = {}
        for field, value in self.request.query_params.items():
            filters[field] = value
        return Authors.objects.filter(**filters)

    def list(self, request, *args, **kwargs):
        model_fields = [field.name for field in Authors._meta.get_fields()]
        if any(field not in model_fields for field in list(self.request.query_params.keys())):
            return Response({"message": "Bad request. Verify the query params"}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
