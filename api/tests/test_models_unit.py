from django.test import TestCase
from api.models import Books, Authors


class BookModelTest(TestCase):

    def setUp(self):
        self.author = Authors.objects.create(name="Author Name")  # Cria um autor
        self.book = Books.objects.create(title="Test Book", author=self.author)  # Atribui o autor ao livro

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author.name, "Author Name")  # Verifica o nome do autor

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")
