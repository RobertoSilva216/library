# library/tests/test_models.py

import pytest
import os
import sys
import django

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()
from api.models import Books, Authors

author_name1 = 'Author name 5'
author_name2 = 'Author name 6'
book_title1 = 'Test Book 5'
book_title2 = 'Test Book 6'

@pytest.mark.django_db
def test_book_creation():
    author = Authors.objects.create(name=author_name1)  # Cria um autor
    book = Books.objects.create(title=book_title1, author=author)  # Atribui o autor ao livro

    assert book.title == book_title1
    assert book.author.name == author_name1  # Verifica o nome do autor

@pytest.mark.django_db
def test_book_str():
    author = Authors.objects.create(name=author_name2)  # Cria um autor
    book = Books.objects.create(title=book_title2, author=author)  # Atribui o autor ao livro

    assert str(book) == book_title2
