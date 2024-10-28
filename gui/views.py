from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from .forms import LoginForm
from api.models import Books
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})


def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def coletar_dados_livros(request, year_to_filter):
    if not year_to_filter or year_to_filter == "0":
        year_to_filter = None
    # URL onde a tabela de livros está localizada
    books_url = "https://api.vrltech.com.br/books"

    # Inicialização do WebDriver
    driver = webdriver.Chrome()  # Altere para o WebDriver do navegador que você usa

    try:
        # Passo 1: Acessar a URL com a tabela de livros
        driver.get(books_url)
        time.sleep(2)  # Aguardar a página carregar

        # Passo 2: Coletar dados da tabela de livros
        books = []
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")  # Ajuste o XPath conforme necessário

        for row in rows:
            title = row.find_element(By.XPATH, "./td[1]").text
            author = row.find_element(By.XPATH, "./td[2]").text
            year = row.find_element(By.XPATH, "./td[3]").text
            description = row.find_element(By.XPATH, "./td[4]").text

            if not year_to_filter or int(year_to_filter) == int(year):
                books.append({
                    "title": title,
                    "author": author,
                    "description": description,
                    "year": year,
                })

        # Passo 3: Salvar dados coletados em arquivo JSON
        with open("books_data.json", "w") as file:
            json.dump(books, file, indent=4, ensure_ascii=False)

        return JsonResponse({"message": "Dados coletados com sucesso."})
    except Exception as e:
        return JsonResponse({"error": f"Erro ao coletar dados: {str(e)}"}, status=500)
    finally:
        # Encerrar o WebDriver
        driver.quit()
