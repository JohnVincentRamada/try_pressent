from django.shortcuts import render

def birthday(request):
    return render(request, 'index.html')