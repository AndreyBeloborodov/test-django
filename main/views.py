from django.shortcuts import render

from .models import Emotion, Question

def indexHome(request):
    return render(request, 'main/indexHome.html')

def indexTesting(request):
    question = Question.objects.order_by('?')[0]
    return render(request, 'main/indexTesting.html', {'question': question})

def indexGood(request):
    emotion = Emotion.objects.filter(positive=True).order_by('?')[0]
    return render(request, 'main/indexGood.html', {'emotion': emotion})

def indexBad(request):
    emotion = Emotion.objects.filter(positive=False).order_by('?')[0]
    return render(request, 'main/indexBad.html', {'emotion': emotion})


