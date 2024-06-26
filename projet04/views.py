from django.shortcuts import render


def index(request):
    return render(request, "projet04/index.html")