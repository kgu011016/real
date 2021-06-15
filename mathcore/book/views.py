from django.shortcuts import render
from django.http import HttpResponse
from .models import BookList


# Create your views here.
def bookprint(request) :
    return render(request, 'book/printmenu.html')


def booklist(request) :
    booklistmem = BookList.objects.all()
    context = {'booklistmem' : booklistmem}
    return render(request, 'book/booklist.html', context)
