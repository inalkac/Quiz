from django.shortcuts import render, redirect
from django.http import Http404
from .models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'quizdb/index.html', context)

def quiz(request, category_name):
    try:
        category = Category.objects.filter(name = category_name).first()
        context = {'category' : category}
        return render(request, 'quizdb/quiz.html', context)
    except Category.DoesNotExist:
        raise Http404("No category")


