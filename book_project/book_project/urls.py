from django.contrib import admin
from django.urls import path
from reader import views as reader_views
from book import views as book_views

urlpatterns = [
    path('', reader_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('books/', book_views.book_list, name='book_list'),
]


