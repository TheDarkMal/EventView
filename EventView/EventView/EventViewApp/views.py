from django.shortcuts import render

# Create your views here.


def cargar_inicio(request):
    return render(request, "EventViewApp/index.html")