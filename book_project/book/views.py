import json
from django.shortcuts import render

def book_list(request):
    with open('books_data.json') as file:
        books = json.load(file)
    return render(request, 'book/book_list.html', {'books': books})
