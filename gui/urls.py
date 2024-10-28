from django.urls import path
from .views import LoginView, book_list, coletar_dados_livros

urlpatterns = [
    path('login', LoginView.as_view(), name='gui-login'),
    path('books', book_list, name='gui-book-list'),
    path('coletar-dados-livros/<int:year_to_filter>', coletar_dados_livros, name='coletar-dados-livros'),
]
