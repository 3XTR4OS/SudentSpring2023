# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import scripts
import re
import scripts.TestQuestions
import scripts.temperament


# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, 'test_href.html')


def input_from(request):
    return render(request, 'input_form.html')
    # return render(request, 'test_href.html')


def search(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            return HttpResponse(f'Вы хотели найти {request.GET["q"]}')
        else:
            return HttpResponse('Вы отправили пустую форму')


def quest_input(request):
    user_answers = []
    print(*request.POST.items())
    for i, answer in request.POST.items():
        number = re.findall(r'[0-9]+', i)
        if not len(number):
            pass
        else:
            user_answers.append(answer)

    user_answers = [bool(True) if i == 'Да' else bool(False) for i in user_answers]
    extraversion_score, neuroticism_score, lie_score = scripts.temperament.check_answers(user_answers)
    temperament = scripts.temperament.temperament_calculate(extraversion_score, neuroticism_score, lie_score)

    temperament_discritpion = scripts.temperament.get_temperament_text(temperament[0], temperament[-1])
    return HttpResponse(temperament_discritpion)
