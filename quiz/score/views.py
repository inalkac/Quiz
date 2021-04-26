from django.shortcuts import render, redirect
from .lib import get_optionIdList
from quizdb.models import Category

# Create your views here.
def score(request):
    if request.method == "POST":
        result = list(dict(request.POST).values())
        categoryId, result = get_optionIdList(result)
        category = Category.objects.get(id = categoryId)
        score = 0 # user score
        check_list = category.check_list()
        for item in result:
            if item in check_list:
                score +=1
        score = int((score*100)/len(check_list))
        context = {
            'score' : score
        }
        return render(request, "score/index.html", context)
    else:
        return redirect('login')
    