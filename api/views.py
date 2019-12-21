from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Author


def index(request):
    author_list = Author.objects.all()
    output = ', '.join([q.first_name for q in author_list])
    return HttpResponse(output)
