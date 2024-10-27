from django.views import View
from django.shortcuts import render
from .forms import LoginForm
from api.models import Books


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})


def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

