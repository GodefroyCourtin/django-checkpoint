from django.shortcuts import render
from .models import Voyage, Step, Linkstep

# Create your views here.
def acceuil(request):
    # voyages = Voyage.objects.all()
    voyages = (
        Voyage.objects.prefetch_related("step_set")
        .prefetch_related("step_set__linkstep_set")
        .order_by("-end_date")
    )

    # voyages = Linkstep.objects.select_related("step").all()
    # .prefetch_related('step_set').prefetch_related('linkstep_set')
    context = {"voyages": voyages}
    return render(request, "travels/acceuil.html", context)


def travel(request):
    voyages = Voyage.objects.prefetch_related("step_set").prefetch_related(
        "step_set__linkstep_set"
    )
    context = {"voyages": voyages}
    return render(request, "travels/travel.html", context)
