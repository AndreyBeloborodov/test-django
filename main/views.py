from django.shortcuts import render


def indexHome(request):
    return render(request, 'main/indexHome.html')
