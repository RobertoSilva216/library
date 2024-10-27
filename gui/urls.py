from django.urls import path
from .views import LoginView, book_list

urlpatterns = [
    path('login', LoginView.as_view(), name='gui-login'),
    path('books', book_list, name='gui-book-list'),
]
