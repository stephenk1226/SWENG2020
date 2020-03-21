from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
#from pages.gutenbergtest import getBookTextByNumber
from .gutenbergtest import *


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def editor_view(request , book_num):
    # if request.is_ajax() and request.method == "POST":
    #     textSelected = request.POST['text']
    name = Book.get_book_name(book_num)
    return render(request, "editor.html", {'content':[getBookTextByNumber(book_num, False)],'name': name})

def Book_view(request):
  books = Book.objects.all()
  args = {
      'books' : books
  }
  return render(request, "home.html", args)