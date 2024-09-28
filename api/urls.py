from django.urls import path
from api.views.authors import *
from api.views.books import *
from api.views.favorites import *
from api.views.users import *
from api.views.auth import *

urlpatterns = [
    # Books
    path('books', BookListCreateView.as_view(), name='books-list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),

    # Authors
    path('authors', AuthorListCreateView.as_view(), name='authors-list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),

    # Authentication
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),

    # Favorites and Recommendations
    path('favorites', FavoriteBooksListView.as_view(), name='favorites'),
    path('favorites/<int:pk>', FavoriteBooksDetailView.as_view(), name='favorites'),
    path('recommendations', RecommendationView.as_view(), name='recommendations'),
]
