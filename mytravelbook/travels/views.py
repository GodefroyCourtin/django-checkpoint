from django.shortcuts import render

# Create your views here.
def acceuil(request):
    context = {}
    return render(request, "travels/acceuil.html", context)


def travel(request):
    context = {}
    return render(request, "travels/travel.html", context)
