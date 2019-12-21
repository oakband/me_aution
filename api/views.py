from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Author
from django.template import loader


def index(request):
    author_list = Author.objects.all()
    # output = ', '.join([q.first_name for q in author_list])
    # return HttpResponse(output)
    template = loader.get_template('api/index.html')
    context = {
        'author_list': author_list,
    }
    # return HttpResponse(template.render(context, request))
    # 另外一种直接的方法是用view的render方法，加载模版
    return render(request, 'api/index.html', context)
