from django.shortcuts import render
from django.http import HttpResponse
from learn import models
# Create your views here.


def hello(request):
    return render(request, 'index.html')


def index(request):
    book_index = models.Book.objects.all().order_by('-id')
    context = {
            'book_index': book_index,
    }
    return render(request, 'index.html', context)

