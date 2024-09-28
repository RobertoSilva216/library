from rest_framework import generics, permissions, status
from api.models import Favorites, Books
from api.serializers import FavoriteSerializer, FavoriteSerializerOut, BookSerializer
from rest_framework.response import Response
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FavoriteBooksListView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request == 'GET':
            return FavoriteSerializer
        return FavoriteSerializerOut

    def get_queryset(self):
        return Favorites.objects.select_related('book', 'user').filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if Favorites.objects.filter(user=request.user).count() >= 20:
            return Response({'message': "You can't favorite more than 20 books"}, status=status.HTTP_400_BAD_REQUEST)
        book_id = request.data['book']
        favorite, created = Favorites.objects.get_or_create(user=request.user, book_id=book_id)
        if not created:
            favorite.delete()
        return Response({"message": "Favorite updated successfully"})


class FavoriteBooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.select_related('book', 'user').all()
    serializer_class = FavoriteSerializerOut
    permission_classes = [permissions.IsAuthenticated]


class RecommendationView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_favorites = Favorites.objects.filter(user=self.request.user)
        favorite_books = [fav.book for fav in user_favorites]

        if not favorite_books:
            return Books.objects.none()

        books = Books.objects.exclude(id__in=[book.id for book in favorite_books])
        favorite_titles = [book.title for book in favorite_books]
        all_titles = [book.title for book in books]

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(favorite_titles + all_titles)

        cosine_sim = cosine_similarity(tfidf_matrix)

        sim_scores = cosine_sim[:len(favorite_titles), len(favorite_titles):].mean(axis=0)

        recommended_indices = sim_scores.argsort()[-5:][::-1]

        books_list = list(books)

        recommended_books = [books_list[i] for i in recommended_indices]
        return recommended_books
