import json
from django.shortcuts import render, HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        return HttpResponseRedirect('/books/')
    return render(request, 'reader/home.html')

def book_list(request):
    with open('reader/books.json') as f:
        books = json.load(f)
    
    return render(request, 'reader/book_list.html', {'books': books})


