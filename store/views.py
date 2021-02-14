from django.shortcuts import render


def index(request):
    context = {
        'header': ''
    }
    return render(request, 'store/index.html', context)
